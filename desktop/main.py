from PyQt5 import QtWidgets as qtw
from controllers.controller import Controller


if __name__ == '__main__':
    app = qtw.QApplication([])

    controller = Controller()
    controller.show_login()

    app.exec()
