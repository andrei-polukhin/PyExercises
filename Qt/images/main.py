import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Qt/images/images.ui", self)
        self.setWindowTitle("Images")
        self.photo = self.findChild(QtWidgets.QLabel, "photo")
        self.cat = self.findChild(QtWidgets.QPushButton, "catButton")
        self.dog = self.findChild(QtWidgets.QPushButton, "dogButton")
        # Initializing methods on pushing the buttons
        self.cat.clicked.connect(self.show_cat)
        self.dog.clicked.connect(self.show_dog)

    def show_dog(self):
        self.photo.setPixmap(QtGui.QPixmap("./Qt/images/dog.jpg"))

    def show_cat(self):
        self.photo.setPixmap(QtGui.QPixmap("./Qt/images/cat.jpg"))


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
