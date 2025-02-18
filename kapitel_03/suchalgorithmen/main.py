from PySide6.QtWidgets import QApplication, QMainWindow
from qt.mainform import Ui_mainWindow

class FormMain(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication()
formMain = FormMain()
formMain.show()
app.exec()