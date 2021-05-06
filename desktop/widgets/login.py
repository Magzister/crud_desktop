from pyuic5_files.login import Ui_Authentication

from PyQt5 import QtWidgets as qtw


class LoginWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Authentication()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.authentication)

    def authentication(self):
        qtw.QMessageBox.information(self, 'Success', 'Try to log in.')


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec()
