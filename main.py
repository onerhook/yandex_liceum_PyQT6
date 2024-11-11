import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from database import DatabaseManager
from csv_handler import CSVHandler
from image_handler import ImageHandler
from exceptions import InvalidDataError

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db_manager = DatabaseManager("library.db")
        self.csv_handler = CSVHandler()
        self.image_handler = ImageHandler()

        self.setup_signals()

    def setup_signals(self):
        # Привязка действий к кнопкам
        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.searchButton.clicked.connect(self.search_books)
        self.ui.importCSVButton.clicked.connect(self.import_csv)
        self.ui.exportCSVButton.clicked.connect(self.export_csv)

    def add_book(self):
        try:
            title = self.ui.titleLineEdit.text()
            author = self.ui.authorLineEdit.text()
            year = self.ui.yearLineEdit.text()
            image = self.ui.imageLineEdit.text()

            if not title or not author or not year:
                raise InvalidDataError("Все поля должны быть заполнены")

            self.db_manager.add_book(title, author, year, image)
            QMessageBox.information(self, "Успех", "Книга добавлена в базу данных")
        except InvalidDataError as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def search_books(self):
        title = self.ui.titleLineEdit.text()
        books = self.db_manager.search_books(title)
        # Обновление таблицы
        self.ui.booksTable.setRowCount(0)
        for book in books:
            row_position = self.ui.booksTable.rowCount()
            self.ui.booksTable.insertRow(row_position)
            for column, data in enumerate(book):
                self.ui.booksTable.setItem(row_position, column, data)

    def import_csv(self):
        try:
            file_path = self.ui.csvFilePath.text()
            books = self.csv_handler.import_books(file_path)
            for book in books:
                self.db_manager.add_book(*book)
            QMessageBox.information(self, "Успех", "Книги импортированы из CSV")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def export_csv(self):
        try:
            file_path = self.ui.csvFilePath.text()
            books = self.db_manager.get_all_books()
            self.csv_handler.export_books(books, file_path)
            QMessageBox.information(self, "Успех", "Книги экспортированы в CSV")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

def main():
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
