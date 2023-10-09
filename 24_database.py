#IMPORT SQLITE3 MODULE
import sqlite3 as sql

#CREATE AND CONNECT TO DATABASE FILE
connect = sql.connect('data/jumia.db')
cursor = connect.cursor()

#DELETE TABLE
query = """
DROP TABLE IF EXISTS products
"""

cursor.execute(query)

#CREATE TABLE
query = """
CREATE TABLE IF NOT EXISTS products(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 product TEXT NOT NULL UNIQUE,
 price REAL NOT NULL,
 date TEXT DEFAULT CURRENT_TIMESTAMP
)
"""

cursor.execute(query)

#CREATE RECORDS
query = """
INSERT INTO products (product,price)
VALUES ('PEPSI',150.0), ('apple',200.0),('sardine',500.0)('short bread',1400.0)('chicken',2500.0)

"""
cursor.execute(query)

#VIEW RECORDS
query = """
SELECT * FROM products
"""
cursor.excute(query)
result_set = cursor.fetchall ()
print (result_set)
