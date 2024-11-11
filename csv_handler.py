import csv

class CSVHandler:
    def import_books(self, file_path):
        books = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                books.append(row)
        return books

    def export_books(self, books, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for book in books:
                writer.writerow(book)
