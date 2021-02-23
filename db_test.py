import sqlite3 

conn = sqlite3.connect("/home/kalki/Desktop/School_Karni/verifica.db")

c = conn.cursor()

c.execute("SELECT * FROM user")
data = c.fetchall()
print(data)

conn.commit()

conn.close()