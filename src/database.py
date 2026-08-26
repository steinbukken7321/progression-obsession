import sqlite3
import os

class DatabaseManager:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.init_db()

    def get_db_path(self):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_path, "data")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return os.path.join(data_dir, "obsession.db")

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Cria a tabela base se ela não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        
        # Verifica automaticamente se a coluna character_class existe. Se não existir, adiciona sozinha!
        cursor.execute("PRAGMA table_info(users)")
        columns = [col[1] for col in cursor.fetchall()]
        if "character_class" not in columns:
            cursor.execute("ALTER TABLE users ADD COLUMN character_class TEXT DEFAULT NULL")

        conn.commit()
        conn.close()

    def authenticate(self, username, password):
        if not username or not password:
            return None
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, character_class FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user

    def register_user(self, username, password):
        if not username or not password:
            return False, "Preencha todos os campos."
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return True, "Soul created successfully!"
        except sqlite3.IntegrityError:
            return False, "Soul ID already exists."

    def save_user_class(self, user_id, character_class):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET character_class = ? WHERE id = ?", (character_class, user_id))
        conn.commit()
        conn.close()