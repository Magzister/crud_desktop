from pyuic5_files.login import Ui_Authentication
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import requests


LOGIN_URL = 'http://localhost:8000/auth/login/'


class LoginWindow(qtw.QWidget):

    login_signal = qtc.pyqtSignal(str, str, str)
    registration_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Authentication()
        self.ui.setupUi(self)

        self.ui.username_error_label.setHidden(True)
        self.ui.password_error_label.setHidden(True)

        self.ui.username_edit.setText('magzister')
        self.ui.password_edit.setText('12345678abc')

        self.ui.login_button.clicked.connect(self.authentication)
        self.ui.registration_button.clicked.connect(self.registration)

    def authentication(self):
        self.ui.username_error_label.setHidden(True)
        self.ui.password_error_label.setHidden(True)

        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        data = {
            'username': username,
            'password': password,
        }
        response = requests.post(LOGIN_URL, data)
        if response.status_code == 200:
            refresh_token = response.json().get('refresh', None)
            access_token = response.json().get('access', None)
            self.login(username, access_token, refresh_token)
        elif response.status_code == 400:
            username_errors = response.json().get('username', None)
            password_errors = response.json().get('password', None)
            if username_errors:
                self.ui.username_error_label.setText(username_errors[0])
                self.ui.username_error_label.setHidden(False)
            if password_errors:
                self.ui.password_error_label.setText(password_errors[0])
                self.ui.password_error_label.setHidden(False)
        elif response.status_code == 401:
            qtw.QMessageBox.information(self, 'Failure', response.json().get('detail', None))

    def registration(self):
        self.registration_signal.emit()

    def login(self, username, access_token, refresh_token):
        self.login_signal.emit(
            username,
            access_token,
            refresh_token
        )

    def success_register(self, username):
        self.ui.username_edit.setText(username)
        self.ui.password_edit.setText('')


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec()
