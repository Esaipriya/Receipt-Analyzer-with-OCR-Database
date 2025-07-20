import sqlite3

def create_table():
    conn = sqlite3.connect("receipts.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            id INTEGER PRIMARY KEY,
            vendor TEXT,
            date TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_data(vendor, date, amount):
    conn = sqlite3.connect("receipts.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO receipts (vendor, date, amount) VALUES (?, ?, ?)", (vendor, date, float(amount)))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect("receipts.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM receipts")
    rows = cur.fetchall()
    conn.close()
    return rows
