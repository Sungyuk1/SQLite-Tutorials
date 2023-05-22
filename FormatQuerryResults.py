import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  

c.execute("SELECT * FROM customers")
#c.fetchone() # last item in the table
#c.fetchmany(3) # Get 3 items
items = c.fetchall() # Get all item in the table
print("Name " + "\t\tEMAIL")
print("--------" + "\t\t---------")
for item in items:
    print(item[0] + " " + item[1] + "\t\t" + item[2])

for item in items:
    print(item)

conn.commit()
conn.close()
print("Command Executed")



