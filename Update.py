import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  

c.execute("""
    UPDATE customers SET first_name = 'Bob' WHERE last_name = 'Elder'
""")
conn.commit()

c.execute("SELECT rowid, * FROM customers")   #This way to show rowid
items = c.fetchall()
for item in items:
    print(item)
    
conn.close()
print("Command Executed")



#c.execute("DROP TABLE customers") - how to delete a table