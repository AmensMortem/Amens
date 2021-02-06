import sys
import requests

from templates.mainDesign import Ui_Form
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class App(QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.outButton.clicked.connect(self.getImage)

    def getImage(self):
        coords = self.xInput.text() + ',' + self.yInput.text()
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



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())