from PyQt6.QtGui import QImage
from PyQt6.QtCore import Qt

class ImageHandler:
    def load_image(self, image_path):
        image = QImage(image_path)
        return image
