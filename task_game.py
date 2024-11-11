from PyQt6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QPushButton, QTimer, QLabel, QSpinBox
from PyQt6.QtCore import QTime


class TaskGame(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мини-игра: Управление временем")

        # Время для игры
        self.time_left = 30  # Время в секундах
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Элементы интерфейса
        self.layout = QVBoxLayout()
        
        self.timer_label = QLabel(f"Оставшееся время: {self.time_left} секунд", self)
        self.layout.addWidget(self.timer_label)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Введите название задачи")
        self.layout.addWidget(self.task_input)

        self.priority_input = QSpinBox(self)
        self.priority_input.setRange(1, 5)
        self.priority_input.setPrefix("Приоритет: ")
        self.layout.addWidget(self.priority_input)

        self.deadline_input = QLineEdit(self)
        self.deadline_input.setPlaceholderText("Введите дедлайн (YYYY-MM-DD)")
        self.layout.addWidget(self.deadline_input)

        self.start_button = QPushButton("Начать задачу", self)
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

    def start_game(self):
        """Запуск игры"""
        self.timer.start(1000)  # Таймер каждую секунду
        self.start_button.setEnabled(False)
        self.task_input.setEnabled(True)
        self.priority_input.setEnabled(True)
        self.deadline_input.setEnabled(True)

    def update_timer(self):
        """Обновление времени"""
        self.time_left -= 1
        self.timer_label.setText(f"Оставшееся время: {self.time_left} секунд")

        if self.time_left <= 0:
            self.timer.stop()
            self.game_over()

    def game_over(self):
        """Окончание игры"""
        task_name = self.task_input.text()
        priority = self.priority_input.value()
        deadline = self.deadline_input.text()

        if task_name and priority and deadline:
            self.accept_task(task_name, priority, deadline)
        else:
            self.reject_task()

    def accept_task(self, task_name, priority, deadline):
        """Задача добавлена в систему"""
        print(f"Задача '{task_name}' добавлена с приоритетом {priority} и дедлайном {deadline}!")
        self.close()

    def reject_task(self):
        """Задача не была добавлена"""
        print("Время истекло, задача не была добавлена!")
        self.close()
