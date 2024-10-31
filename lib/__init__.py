import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

from database import create_tables

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")
