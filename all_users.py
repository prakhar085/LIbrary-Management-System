


class All_users:
    def __init__(self, lib_database):
        self.db = lib_database
        self.db_cursor = lib_database.cursor()

    def add_user(self, username, firstname, lastname, phone, password):
        sql_form2 = "SELECT * FROM user WHERE username = '{}'".format(username)
        self.db_cursor.execute(sql_form2)
        res = list(self.db_cursor)
        if res:
            print("You are already a user. ")
            return
        sql_form = "Insert into user(username, first_name, last_name, phone_no, password) values(%s, %s, %s, %s, %s)"
        us = [(username, firstname, lastname, phone, password), ]
        self.db_cursor.executemany(sql_form, us)
        self.db.commit()
        print("User added successfully :)")
        return


