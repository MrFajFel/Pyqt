#pyuic6 layout.ui -o layout.py
import sys

from PyQt6.QtWidgets import QWidget, QApplication

from layout import Ui_Dialog


class Myform(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.okButton.clicked.connect(self.button_click)
        self.show()


    def button_click(self):
        name = self.ui.nameEdit.text()
        self.ui.rezultLabel.setText(f'Witaj {name}')



if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = Myform()
    sys.exit(app.exec())




