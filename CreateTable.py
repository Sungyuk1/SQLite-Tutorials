import sqlite3

#You can also make a database that is not permanent and only in memory. But this will delete afterwards and will not be permanent
#conn = sqlite3.connect(':memory:')

#also pwd - print working directory in mac terminal

#Create a connection to our database. Pass in name of database you want to make. It will connect if already there, or make one if it isn't there 
conn = sqlite3.connect('customer.db')

#Think of a table as an excel spreadsheet. Just has rows and columns

#Need to create a cursor before creating table. It tells database what you want to do. 
c = conn.cursor()  

#Create a table. The doc strings let you write multiple lines
c.execute("""
    CREATE TABLE customers (
    first_name text, 
    last_name text,
    email text
    )
""")   #execute command in sql

#commit our command
conn.commit()

#close our connection. - It will close itself when file stops running by default
conn.close()



