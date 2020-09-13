import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Adding buttons")
        self.setWindowIcon(QIcon("python.png"))

    def add_button(self):
        button = QtWidgets.QPushButton(self)
        button.setText("Click me")
        button.adjustSize()
        button.clicked.connect(self.clicked)

    @staticmethod
    def clicked():
        print("Clicked")


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.add_button()
    gui.show()
    sys.exit(app.exec_())


run()
