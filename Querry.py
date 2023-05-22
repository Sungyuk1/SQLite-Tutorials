import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  

#you can also use LIKE command to get items where it matches a just a certain part
c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
#c.fetchone() # last item in the table
#c.fetchmany(3) # Get 3 items
items = c.fetchall() # Get all item in the table
print("Name " + "\t\tEMAIL")
print("--------" + "\t\t---------")

for item in items:
    print(item)

conn.commit()
conn.close()
print("Command Executed")



