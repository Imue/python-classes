import sqlite3 as sql

connect = sql.connect('data/jumia.txt')
cursor = connect.cursor()

query =  """
DROP TABLE IF EXISTS orders
"""
cursor.execute(query)

query = """
CREATE TABLE IF NOT EXISTS orders(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product_id INTEGER NOT NULL,
  unit_price REAL NOT NULL,
  qty REAL DEFAULT 1,
  date TEXT CURRENT_TIMESTAMP

)
"""
cursor.execute(query)

query = """
INSERT INTO ORDERS (products_id, unit_price, qty)
VALUES (1,150.0,12),
(2, 200.0, 15),
(3, 500.0, 18),
(4, 1400.0, 25),
(5, 3500.0, 8)
"""
cursor.execute(query)

query = """
SELECT * FROM orders
"""

cursor.execute(query)

result_set = cursor.fetchall()
print(result_set)
                      
