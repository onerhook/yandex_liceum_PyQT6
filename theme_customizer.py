from PyQt6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtGui import QColor, QPalette


class ThemeCustomizer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Настройки темы")

        # Интерфейс
        self.layout = QVBoxLayout()

        # Метка
        self.label = QLabel("Выберите тему:", self)
        self.layout.addWidget(self.label)

        # Выпадающий список с темами
        self.theme_selector = QComboBox(self)
        self.theme_selector.addItems(["Стандартная", "Темная", "Светлая", "Пользовательская"])
        self.theme_selector.currentIndexChanged.connect(self.change_theme)
        self.layout.addWidget(self.theme_selector)

        # Кнопка для применения кастомной темы
        self.apply_button = QPushButton("Применить кастомные цвета", self)
        self.apply_button.clicked.connect(self.apply_custom_colors)
        self.layout.addWidget(self.apply_button)

        # Размещение
        self.setLayout(self.layout)

    def change_theme(self, index):
        """Меняем тему интерфейса в зависимости от выбора"""
        palette = QPalette()

        if index == 0:  # Стандартная
            self.setStyle("Fusion")
            palette.setColor(QPalette.ColorRole.Window, QColor(240, 240, 240))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))

        elif index == 1:  # Темная
            self.setStyle("Fusion")
            palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))

        elif index == 2:  # Светлая
            self.setStyle("Fusion")
            palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 0, 0))

        elif index == 3:  # Кастомная
            self.apply_custom_colors()

        self.setPalette(palette)

    def apply_custom_colors(self):
        """Применяем пользовательские цвета"""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 128, 128))  # Тёмный зелёный
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # Белый текст
        self.setPalette(palette)
