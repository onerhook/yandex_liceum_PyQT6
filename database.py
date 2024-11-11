import sqlite3

class Database:
    def __init__(self, db_name='tasks.db'):
        """Инициализация подключения к базе данных."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        """Создание таблицы задач в базе данных, если она не существует."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            deadline TEXT,
            priority INTEGER,
            status TEXT,
            notes TEXT
        )
        """)
       
