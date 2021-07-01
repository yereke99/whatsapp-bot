import mysql.connector, os
from mysql.connector import errorcode
from sys import exit

user_data = {}

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "121212",
        port = "3306",
        database = "data"
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Пайдаланушы аты немесе пароль қате!")
        exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DATABASE does not exit")
        exit()
    else:
        print(err)
        exit()

cursor = db.cursor()


#cursor.execute("CREATE DATABASE data")

#cursor.execute("CREATE TABLE Link (id INT AUTO_INCREMENT PRIMARY KEY, link VARCHAR(500), client_number VARCHAR(30))")
#db.commit()

#cursor.execute("CREATE TABLE CLIENT (id INT AUTO_INCREMENT PRIMARY KEY, money VARCHAR(100), kvi VARCHAR(50), data VARCHAR(50), time VARCHAR(10), who VARCHAR(50),  owner_name VARCHAR(25))")
#db.commit()



#cursor.execute("CREATE TABLE hashtags (id INT AUTO_INCREMENT PRIMARY KEY, hashtags VARCHAR(255) UNIQUE )")
#db.commit()




#cursor.execute("CREATE TABLE accounts_who_liked_post (id INT AUTO_INCREMENT PRIMARY KEY, instagram_accounts VARCHAR(255) )")
#db.commit()

#cursor.execute("CREATE TABLE hashtag_page (id INT AUTO_INCREMENT PRIMARY KEY, Instagram_Accounts VARCHAR(255) )")
#db.commit()

#cursor.execute("CREATE TABLE accounts (id INT AUTO_INCREMENT PRIMARY KEY, usr VARCHAR(255) )")
#db.commit()


# DELETE ALL RECORD
#cursor.execute("DELETE FROM accounts ")
#db.commit()
#print('Записи удалена!')











class User:
    def __init__(self, login):
        self.login = login
        self.password = ''





