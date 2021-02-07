import sys
import requests

from templates.mainDesign import Ui_Form
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt


class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.scaleInput.setRange(1, 23)
        self.xInput.setSingleStep(0.1)
        self.xInput.setRange(-180, 180)
        self.yInput.setSingleStep(0.1)
        self.yInput.setRange(-180, 180)
        self.outButton.clicked.connect(self.getImage)
        self.getImage()

    def getImage(self):
        coords = self.xInput.text().replace(',', '.') + \
                 ',' + self.yInput.text().replace(',', '.')
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}" \
                      f"&z={self.scaleInput.text()}&l=map"

        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.mapOut.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()

        # Масштабирование с помощь PgDown PgUp
        if key == Qt.Key_PageUp:
            self.scaleInput.setValue(self.scaleInput.value() + 1)
        elif key == Qt.Key_PageDown:
            self.scaleInput.setValue(self.scaleInput.value() - 1)

        # Управление WASD
        if key in {Qt.Key_A, 1060}:
            self.xInput.setValue(self.xInput.value() - 0.1)
        elif key in {Qt.Key_D, 1042}:
            self.xInput.setValue(self.xInput.value() + 0.1)
        elif key in {Qt.Key_S, 1067}:
            self.yInput.setValue(self.yInput.value() - 0.1)
        elif key in {Qt.Key_W, 1062}:
            self.yInput.setValue(self.yInput.value() + 0.1)
        self.getImage()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
