import sys
from PySide6 import QtWidgets
from untitled import Ui_MainWindow # название2 = название2.py, сгенерированный выше


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()