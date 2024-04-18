import sqlite3

class SqliteConnecter():
    def __init__(self, path) -> None:
        self.conn = sqlite3.connect(path)  # Connects or creates a database file.
        self.c = self.conn.cursor()  # Allows the database to be changed