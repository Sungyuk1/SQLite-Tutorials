import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  


many_customers = [('wes', 'Brown', 'wes@gmail.com'),
                   ('Jack', 'Brown', 'wesds@gmail.com'), 
                   ('Joe', 'Brown', 'wefds@gmail.com'),
                       ('Sungu', 'Brown', 'weaas@gmail.com'),]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)  
conn.commit()
conn.close()
print("Command Executed")



