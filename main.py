import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget
from database import Database
from theme_customizer import ThemeCustomizer
from task_game import TaskGame

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Трекер задач")

        # Инициализация базы данных
        self.db = Database()

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

    def load_tasks(self):
        """Загрузка задач из базы данных в таблицу"""
        tasks = self.db.get_all_tasks()
        self.table_widget.setRowCount(len(tasks))
        self.table_widget.setColumnCount(6)

        for row_num, task in enumerate(tasks):
            for col_num, value in enumerate(task[1:]):
                self.table_widget.setItem(row_num, col_num, QTableWidgetItem(str(value)))

    def add_task(self):
        """Добавление новой задачи (например, через жестко заданные данные)"""
        name = "Новая задача"
        deadline = "2024-12-01"
        priority = 3
        status = "Не выполнено"
        notes = "Примечания"
        
        self.db.add_task(name, deadline, priority, status, notes)
        self.load_tasks()

    def open_theme_customizer(self):
        """Открытие окна настройки темы"""
        theme_window = ThemeCustomizer(self)
        theme_window.show()

    def start_game(self):
        """Запуск мини-игры"""
        game_window = TaskGame()
        game_window.exec()

    def closeEvent(self, event):
        """Закрытие программы и сохранение базы данных"""
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())
