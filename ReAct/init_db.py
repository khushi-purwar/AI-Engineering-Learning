import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

# Create the orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    total_amount REAL NOT NULL
)
""")

# Insert 10 dummy records
cursor.executemany("""
INSERT INTO orders
(customer_id, order_date, product_name, quantity, unit_price, total_amount)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (101, '2026-09-01', 'Laptop',       1, 75000.00, 75000.00),
    (102, '2026-09-02', 'Mouse',        2,   800.00,  1600.00),
    (103, '2026-09-03', 'Keyboard',     1,  2500.00,  2500.00),
    (104, '2026-09-04', 'Monitor',      2, 15000.00, 30000.00),
    (105, '2026-09-05', 'Headphones',   3,  2000.00,  6000.00),
    (106, '2026-09-06', 'Webcam',       1,  3500.00,  3500.00),
    (107, '2026-09-07', 'Printer',      1, 12000.00, 12000.00),
    (108, '2026-09-08', 'USB Cable',    5,   300.00,  1500.00),
    (109, '2026-09-09', 'SSD 1TB',      2,  6500.00, 13000.00),
    (110, '2026-09-10', 'Keyboard',     2,  2500.00,  5000.00)
])

conn.commit()

# Optional: verify the records
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)

conn.close()