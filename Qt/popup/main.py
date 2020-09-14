import sys
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pop-up windows")
        uic.loadUi("./Qt/popup/popup.ui", self)
        # Finding the label into our QtDesigner file
        self.label = self.findChild(QtWidgets.QLabel, "myLabel")
        # Finding the button
        self.myButton = self.findChild(QtWidgets.QPushButton, "myButton")
        # Connecting the function on pressing the button
        self.myButton.clicked.connect(self.show_popup)

    def show_popup(self):
        # Initializing the message box
        msg = QMessageBox()
        msg.setWindowTitle("Notification")
        # The main text into the popup window
        msg.setText("You must have clicked that button!")
        # Set a global icon for the popup window
        msg.setIcon(QMessageBox.Information)
        # Add buttons into the popup window
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        # Set the highlighted button
        msg.setDefaultButton(QMessageBox.Ok)
        # Set text beneath the main text
        msg.setInformativeText("nonsense here")
        # Text on pressing the "Show details..." button
        msg.setDetailedText("So this programme does nothing, still feeling lucky?")
        # Adding a triggering to the function on clicking the button in
        # the pop-up window
        msg.buttonClicked.connect(self.popup_button_triggered)
        x = msg.exec_()

    def popup_button_triggered(self, i):
        self.label.setText(i.text())


def run():
    app = QApplication(sys.argv)
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


run()
