import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QMenu, QAction, QFileDialog
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QColor, QPalette
import sqlite3
from theme_customizer import ThemeCustomizer
from task_game import TaskGame

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Трекер задач")

        # Инициализация базы данных
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self.setup_db()

        # Основной интерфейс
        self.table_widget = QTableWidget(self)
        self.load_tasks()

        self.add_task_button = QPushButton("Добавить задачу", self)
        self.add_task_button.clicked.connect(self.add_task)

        self.start_game_button = QPushButton("Мини-игра", self)
        self.start_game_button.clicked.connect(self.start_game)

        self.theme_button = QPushButton("Настроить тему", self)
        self.theme_button.clicked.connect(self.open_theme_customizer)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_task_button)
        layout.addWidget(self.start_game_button)
        layout.addWidget(self.theme_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setup_db(self):
        """Создание таблицы для задач в базе данных"""
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
        self.conn.commit()

    def load_tasks(self):
        """Загрузка задач из базы данных в таблицу"""
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        self.table_widget.setRowCount(len(tasks))
        self.table_widget.setColumnCount(6)

        for row_num, task in enumerate(tasks):
            for col_num, value in enumerate(task[1:]):
                self.table_widget.setItem(row_num, col_num, QTableWidgetItem(str(value)))

    def add_task(self):
        """Добавление новой задачи (простой пример)"""
        name = "Новая задача"
        deadline = "2024-12-01"
        priority = 3
        status = "Не выполнено"
        notes = "Примечания"
        
        self.cursor.execute("INSERT INTO tasks (name, deadline, priority, status, notes) VALUES (?, ?, ?, ?, ?)",
                            (name, deadline, priority, status, notes))
        self.conn.commit()
        self.load_tasks()

    def open_theme_customizer(self):
        """Открытие окна настроек темы"""
        theme_window = ThemeCustomizer()
        theme_window.show()

    def start_game(self):
        """Запуск мини-игры"""
        game_window = TaskGame()
        game_window.exec()

    def closeEvent(self, event):
        """Закрытие программы и сохранение базы данных"""
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())
