import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path='data/obsession.db'):
        self.db_path = db_path
        # Ensure data folder exists
        if not os.path.exists('data'):
            os.makedirs('data')
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Table for users and their progression stats
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
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if user:
            if user[2] == password:
                conn.close()
                return user # Login success
            conn.close()
            return "WRONG_PASS"
        
        # Auto-register if user doesn't exist
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        new_user = cursor.fetchone()
        conn.close()
        return new_user

    def save_progress(self, user_id, stats):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET gold = ?, xp = ?, level = ?, strength = ?, addiction_level = ?
            WHERE id = ?
        ''', (stats['gold'], stats['xp'], stats['level'], stats['strength'], stats['addiction'], user_id))
        conn.commit()
        conn.close()