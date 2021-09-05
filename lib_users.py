from collections import defaultdict
import mysql.connector
from datetime import datetime
date_format = "%m/%d/%Y"

from all_users import All_users

class Library_users(All_users):
    def __init__(self, lib_database):
        super().__init__(lib_database)
        self.db = lib_database
        self.db_cursor = lib_database.cursor()

    def __add_books(self, author, title, quantity, price):
        key = "{}|{}".format(author, title)
        sql_form = "SELECT * FROM books1 WHERE authtit = '{}'".format(key)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res:
            final_quantity = quantity + res[0][-2]
            sql_form = "UPDATE books1 SET quantity = {} WHERE authtit = '{}'".format(final_quantity, key)
            self.db_cursor.execute(sql_form)
            self.db.commit()
            return
        sql_form = "Insert into books1(authtit, quantity, price) values(%s, %s, %s)"
        book = [(key, quantity, price), ]
        self.db_cursor.executemany(sql_form, book)
        self.db.commit()
        return

    def borrow(self):
        username = input("Enter username: ")
        pasword = input("Eneter password: ")
        self.db_cursor.execute("SELECT * from user where username='{}'".format(username))
        res = list(self.db_cursor)
        if not res or res[0][-1] != pasword:
            print("Incorrect username and password. ")
            return
        author = input("Enter the author name: ")
        title = input("Enter the title name: ")
        key = '{}|{}'.format(author, title)
        sql_check = "SELECT * from users_who_borrowed_book_3 where username='{}' and authtit='{}'".format(username, key)
        self.db_cursor.execute(sql_check)
        res = list(self.db_cursor)
        if res:
            print("You have already borrowed {} by {}".format(title, author))
            return
        sql_form = "SELECT * FROM books1 WHERE authtit = '{}'".format(key)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if not res:
            print("Sorry {}, we don't have {} by {}".format(username, author, title))
            return
        final_quantity = res[0][-2] - 1
        if final_quantity == 0:
            sql_form = "DELETE * from books1 where authtit = '{}'".format(key)
            self.db_cursor.execute(sql_form)
            self.db.commit()
        else:
            sql_form = "UPDATE books1 SET quantity = {} WHERE authtit = '{}'".format(final_quantity, key)
            self.db_cursor.execute(sql_form)
            self.db.commit()
        date = input("Enter today's date: ")
        sql_set = "Insert into users_who_borrowed_book_3(username, authtit, date, price) values(%s, %s, %s, %s)"
        data = [(username, key, date, res[0][-1]), ]
        self.db_cursor.executemany(sql_set, data)
        self.db.commit()
        print("Books borrowed successfully")
        return

    def Return_book(self):
        username = input("Enter username: ")
        pasword = input("Eneter password: ")
        self.db_cursor.execute("SELECT * from user where username='{}'".format(username))
        res = list(self.db_cursor)
        if not res or res[0][-1] != pasword:
            print("Incorrect username and password. ")
            return
        sql_form = "SELECT * from users_who_borrowed_book_3 where username='{}'".format(username)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if not res:
            print("You have not borrowed any book")
            return
        #print(res)
        for i in range(len(res)):
            print("press {} for '{} by {}'".format(i + 1, *res[i][1].split("|")))
        print("\n")
        k = int(input())
        if k > len(res):
            print("Invalid Input")
            return
        k -= 1
        key = res[k][1].split("|")
        self.__add_books(key[0], key[1], 1, res[k][-1])
        todays_date = datetime.strptime(input("Enter today's date: "), date_format)
        b = datetime.strptime(res[k][-2], date_format)
        print("Amout to pay: ", res[k][-1] * (todays_date - b).days)
        sql_form = "DELETE from users_who_borrowed_book_3 where username='{}' and authtit = '{}'".format(username, res[k][1])
        self.db_cursor.execute(sql_form)
        self.db.commit()
        return