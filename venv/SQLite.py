import sqlite3

conn = sqlite3.connect('client.db',  check_same_thread=False)
cursor = conn.cursor()

#data = ('1000,00', '12345678910', 'yerek', '12.02.2021', '20:03', '+77471850499')
#l = ('https//twilio.dsjisiasjiasjsiasj/aisias', '15.02.2021 14:47', '+77471850499')


cursor.execute("""
               CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     money varchar(10), 
                                     kvi varchar(15),
                                     name varchar(10)
                                     
                                     
               )
""")

'''cursor.execute("""
       CREATE TABLE links (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           link varchar(500),
                           date_and_time varchar(50),
                           tele_number varchar(12)
       )
""")

'''

'''cursor.execute("""
               INSERT INTO links (link, date_and_time, tele_number) VALUES(?, ?, ?)
""", l)
conn.commit()
'''



'''
cursor.execute(
               """ INSERT INTO clients( 
                                       money, 
                                       kvi,
                                       name,
                                       data,
                                       time,
                                       tele_number
                                       )
                   VALUES(
                          ?,
                          ?,
                          ?,
                          ?,
                          ?,
                          ?
                   )                    
               """,
               data
               )

conn.commit()

'''

