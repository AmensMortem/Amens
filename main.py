import sys

from PyQt5.QtWidgets import QWidget, QApplication


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())