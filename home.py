import mysql.connector
import Admin
import lib_users

lib_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PRA085@dik", #Use your server password.
    database='library_management_system',
)
##creating tables..
'''
my_cursor = lib_database.cursor()
# 1: Books (columns:- [author + title(author|title), quantity, price]
# 2: user (columns:- [username, first_name, last_name, phone_no, password]
# 3: users_who_borrowed_book: [username, authtit, date, price]
# 4: admin (columns:- [username, phone_no. password]

table_admin = "Create table admin(username varchar(255), phone_no varchar(20), password varchar(255))"
table_book = "Create table books1(authtit varchar(255), quantity int(255), price int(100))"
table_user = "Create table user(username varchar(255), first_name varchar(255), last_name varchar(255), phone_no varchar(20), password varchar(255))"
table_users_who_borrowed_book_3 = "Create table users_who_borrowed_book_3(username varchar(255), authtit varchar(255), date varchar(100), price int(100))"
my_cursor.execute(table_book)
my_cursor.execute(table_user)
my_cursor.execute(table_users_who_borrowed_book_3)
my_cursor.execute(table_admin)
'''
admin = Admin.Admin(lib_database)
users = lib_users.Library_users(lib_database)
while True:
    k = int(input("Press 1 for admin section \n"
                  "Press 2 for customer section \n"
                  "Press 0 for exit: \n"))
    if k == 0:
        exit()
    ##proceeding in admin section
    if k == 1:
        kk = int(input("Press 1 for admin registration \n"
                       "Press 2 for adding books \n"
                       "Press 3 for customer registration \n"
                       "Press 4 for main menu \n"
                       "Press 0 for exit: \n"))
        if kk == 0:
            exit()
        if kk == 2:
            author = input("Enter author name: ")
            title = input("Enter title name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter the price for one day: "))
            admin.add_books(author, title, quantity, price)
            continue
        elif kk == 1:
            username = input("Enter username: ")
            phone_no = input("Enter phone number: ")
            password = input("Enter password: ")
            admin.add_admin(username, phone_no, password)
            continue
        elif kk == 3:
            username = input("Enter username: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_no = input("Enter mobile number: ")
            password = input("Enter password: ")
            admin.add_user(username, first_name, last_name, phone_no, password)
            continue
        elif kk == 4:
            continue
        else:
            print("Not valid input")
            continue
    elif k == 2:
        kk = int(input("Press 1 for user registration \n"
                       "Press 2 for borrowing books \n"
                       "Press 3 for returning book \n"
                       "Press 4 for main menu \n"
                       "Press 0 for exit: \n"))
        if kk == 0:
            exit()
        if kk == 1:
            username = input("Enter username: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_no = input("Enter mobile number: ")
            password = input("Enter password: ")
            users.add_user(username, first_name, last_name, phone_no, password)
            continue
        if kk == 2:
            users.borrow()
            continue
        if kk == 3:
            users.Return_book()
            continue
        elif kk == 4:
            continue
        else:
            print("Not valid input ")
            continue

