import sys

from templates.mainDesign import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())