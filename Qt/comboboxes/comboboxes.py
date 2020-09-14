import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comboboxes")
        # Loading the ui file
        uic.loadUi("./Qt/comboboxes/comboboxes.ui", self)
        # Initializing all in-ui objects
        self.label = self.findChild(QtWidgets.QLabel, "myLabel")
        self.comboX = self.findChild(QtWidgets.QComboBox, "comboX")
        self.comboY = self.findChild(QtWidgets.QComboBox, "comboY")
        # Initializing the submit button
        # and triggering the function on pressing
        self.submit = self.findChild(QtWidgets.QPushButton, "myButton")
        self.submit.clicked.connect(self.pressed)
        # Calling all necessary in-class functions
        self.add_item_to_combox()  # Adds the third item
        self.remove_item_from_combox()  # Removes "Hello"

    def add_item_to_combox(self):
        self.comboX.addItem("Hello")

    def remove_item_from_combox(self):
        index = self.comboX.findText("Hello", QtCore.Qt.MatchFixedString)
        self.comboX.removeItem(index)

    def pressed(self):
        x = int(self.comboX.currentText())
        y = int(self.comboY.currentText())
        result = self.calculate_xor(x, y)
        self.label.setText(f"X XOR Y = {result}")

    @staticmethod
    def calculate_xor(x, y):
        if x == y:
            return 0
        return 1


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
