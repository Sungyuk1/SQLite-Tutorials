import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  

c.execute("SELECT * FROM customers")
#c.fetchone() # last item in the table
#c.fetchmany(3) # Get 3 items
print(c.fetchall()) # Get all item in the table

conn.commit()
conn.close()
print("Command Executed")



