from collections import defaultdict
import mysql.connector
from datetime import datetime
date_format = "%m/%d/%Y"

from all_users import All_users


class Admin(All_users):
    def __init__(self, lib_database):
        super().__init__(lib_database)
        self.db = lib_database
        self.db_cursor = lib_database.cursor()

    def add_admin(self, username, phone, password):
        admin_username = input("Enter Admin username: ")
        admin_pasword = input("Enter password: ")
        self.db_cursor.execute("SELECT * from admin where username='{}'".format(admin_username))
        res = list(self.db_cursor)
        if not res or res[0][-1] != admin_pasword:
            print("You don't have authority to add admin. ")
            return
        else:
            sql_form2 = "SELECT * FROM admin WHERE username = '{}'".format(username)
            self.db_cursor.execute(sql_form2)
            res = list(self.db_cursor)
            if res:
                print("You are already a Admin. ")
                return
            sql_form = "Insert into admin(username, phone_no, password) values(%s, %s, %s)"
            us = [(username, phone, password), ]
            self.db_cursor.executemany(sql_form, us)
            self.db.commit()
            print("Admin added successfully :)")
            return

    def add_books(self, author, title, quantity, price):
        username = input("Enter Admin username: ")
        pasword = input("Eneter password: ")
        self.db_cursor.execute("SELECT * from admin where username='{}'".format(username))
        res = list(self.db_cursor)
        if not res or res[0][-1] != pasword:
            print("Incorrect username and password. ")
            return
        key = "{}|{}".format(author, title)
        sql_form = "SELECT * FROM books1 WHERE authtit = '{}'".format(key)
        self.db_cursor.execute(sql_form)
        res = list(self.db_cursor)
        if res:
            final_quantity = quantity + res[0][-2]
            sql_form = "UPDATE books1 SET quantity = {} WHERE authtit = '{}'".format(final_quantity, key)
            self.db_cursor.execute(sql_form)
            self.db.commit()
            print("Books has been added successfully")
            return
        sql_form = "Insert into books1(authtit, quantity, price) values(%s, %s, %s)"
        book = [(key, quantity, price), ]
        self.db_cursor.executemany(sql_form, book)
        self.db.commit()
        print("Books has been added successfully")
        return
