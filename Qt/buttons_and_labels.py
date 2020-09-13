import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Using smart buttons")
        self.setWindowIcon(QIcon("python.png"))
        self.add_label()
        self.add_button()

    def add_label(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("An initial label")
        self.label.adjustSize()
        self.label.move(250, 150)

    def add_button(self):
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me")
        self.button.adjustSize()
        self.button.move(250, 100)
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("The label has changed")
        self.label.adjustSize()


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
