import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("My OOP PyQt programme")
        self.setWindowIcon(QIcon("python.png"))
        self.show()


app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
