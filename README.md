# LIbrary-Management-System
A functional and fully automated Library Management System using Mysql and Concepts of Object Oriented Programming.


Prerequisites
* Python 3.5 or above.
* Mysql server installed in the system. (if not installed https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing).
* Mysql workbench (if not installed https://dev.mysql.com/downloads/workbench/).
* Mysql connector(if not installed use command **pip install mysql-connector-python**.)


## Steps to use Library Management System.
After installing the required softwares and packages we are good to go for using this app.
1.  Create a seperate Database in the Mysql local server(or where you want to use), here it is named as 'library_management_system', you can keep the name what you want, just dont forget to change it in the home.py file (line 9).
1.  We can manually create tables in mysql workbench, or we can code them, I used the later one, code can be found in home.py file for the same.
    here I have created 4 tables, namely "admin", "books1", "user", "users_who_borrowed_book_3".
1.  Add a super user in admin table(This super user will be our main admin of library). This should be done manually using mysql workbech or command line.
1.  We are good to go. Run home.py


Note: Here have used the password of my local sql server in home.py(line 8), You have to use your password.



Format: ![Alt Text](https://drive.google.com/file/d/12VarkOrB-l5ySY2rRJSawt_XdIMAyf3Q/view?usp=sharing)



