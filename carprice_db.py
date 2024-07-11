import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("carprice.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS car (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car TEXT NOT NULL,
    price INTEGER NOT NULL,
    mileage INTEGER NOT NULL
)
''')

# Insert a record into the car table
cursor.execute("INSERT INTO car (car, price, mileage) VALUES (?, ?, ?)",
               ('axio', 123, 123))

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
