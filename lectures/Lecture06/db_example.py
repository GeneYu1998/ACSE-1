import sqlite3

#Connect to/create db file
conn = sqlite3.connect('my_db.sqlite')

cur = conn.cursor()
try:
    cur.execute("CREATE TABLE fruit(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), price INTEGER)")
    print("Table created")
except sqlite3.OperationalError:
    print("Table exists")

# Write some data
cur.execute("INSERT INTO fruit (name, price) VALUES (?,?);", ("apple", 300))

# Read some data
cur.execute("SELECT * FROM fruit;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("SELECT price FROM fruit WHERE id=?;", "1")
row = cur.fetchone()
print('Price:', row)

conn.commit()
cur.close()
conn.close()
