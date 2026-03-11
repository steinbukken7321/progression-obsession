import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='data/obsession.db'):
        self.db_path = db_path
        if not os.path.exists('data'):
            os.makedirs('data')
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                password TEXT,
                gold REAL DEFAULT 10.0,
                xp INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                strength INTEGER DEFAULT 5,
                addiction_level INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()

    def authenticate(self, email, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        return user

    def register_user(self, email, password, confirm_password):
        if password != confirm_password:
            return "PASS_MISMATCH"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            return cursor.fetchone()
        except sqlite3.IntegrityError:
            return "EMAIL_EXISTS"
        finally:
            conn.close()