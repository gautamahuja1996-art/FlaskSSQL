import sqlite3

# let's connect with the database
connection = sqlite3.connect('users.db')

# creating a curson to interact: add,delete,update,read operation on database
cursor = connection.cursor()

# writing a query to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        sno INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# let's commit this to the database
connection.commit()

# let's close the connection
connection.close()