import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()  

c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')") 
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")   
c.execute("INSERT INTO customers VALUES ('Joe', 'Elder', 'joe@codemy.com')")    
conn.commit()
conn.close()
print("Command Executed")



