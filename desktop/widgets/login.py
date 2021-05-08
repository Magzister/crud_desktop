from pyuic5_files.login import Ui_Authentication
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from object_list import ObjectsWindow

import requests

LOGIN_URL = 'http://localhost:8000/auth/login/'


class LoginWindow(qtw.QWidget):

    login = qtc.pyqtSignal(str, str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Authentication()
        self.ui.setupUi(self)

        self.ui.username_error_label.setHidden(True)
        self.ui.password_error_label.setHidden(True)

        self.ui.username_edit.setText('magzister')
        self.ui.password_edit.setText('12345678abc')

        self.ui.login_button.clicked.connect(self.authentication)

    def authentication(self):
        self.ui.username_error_label.setHidden(True)
        self.ui.password_error_label.setHidden(True)

        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(LOGIN_URL, data)
        if response.status_code == 200:
            refresh_token = response.json().get('refresh', None)
            access_token = response.json().get('access', None)
            self.open_objects_window()
            self.login.emit(
                username,
                access_token,
                refresh_token
            )
            self.close()
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

    def open_objects_window(self):
        object_window_widget = ObjectsWindow()
        self.login.connect(object_window_widget.login_message)
        object_window_widget.show()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()

    app.exec()
