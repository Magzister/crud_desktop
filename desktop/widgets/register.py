from pyuic5_files.register import Ui_Registration
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import requests


REGISTER_URL = 'http://localhost:8000/auth/register/'


class RegisterWindow(qtw.QWidget):

    registration_signal = qtc.pyqtSignal(str)
    cancel_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.hide_error_labels()

        self.ui.registration_button.clicked.connect(self.registration)
        self.ui.cancel_button.clicked.connect(self.cancel)

    def registration(self):
        self.hide_error_labels()

        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()
        password2 = self.ui.password_repeat_edit.text()
        email = self.ui.email_edit.text()
        first_name = self.ui.name_edit.text()
        last_name = self.ui.surname_edit.text()

        data = {
            'username': username,
            'password': password,
            'password2': password2,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        response = requests.post(REGISTER_URL, data)
        if response.status_code == 201:
            qtw.QMessageBox.information(self, 'Success', 'Account created!')
            self.register(username)
        if response.status_code == 400:
            self.set_errors(response.json())

    def register(self, username):
        self.registration_signal.emit(username)

    def cancel(self):
        self.cancel_signal.emit()

    def hide_error_labels(self):
        self.ui.username_error_label.setHidden(True)
        self.ui.password_error_label.setHidden(True)
        self.ui.repeat_password_error_label.setHidden(True)
        self.ui.email_error_label.setHidden(True)
        self.ui.name_error_label.setHidden(True)
        self.ui.surname_error_label.setHidden(True)

    def set_errors(self, errors):
        username_errors = errors.get('username')
        password_errors = errors.get('password')
        password2_errors = errors.get('password2')
        email_errors = errors.get('email')
        first_name_errors = errors.get('first_name')
        last_name_errors = errors.get('last_name')

        if username_errors:
            self.ui.username_error_label.setText(username_errors[0])
            self.ui.username_error_label.setHidden(False)
        if password_errors:
            self.ui.password_error_label.setText(password_errors[0])
            self.ui.password_error_label.setHidden(False)
        if password2_errors:
            self.ui.repeat_password_error_label.setText(password2_errors[0])
            self.ui.repeat_password_error_label.setHidden(False)
        if email_errors:
            self.ui.email_error_label.setText(email_errors[0])
            self.ui.email_error_label.setHidden(False)
        if first_name_errors:
            self.ui.name_error_label.setText(first_name_errors[0])
            self.ui.name_error_label.setHidden(False)
        if last_name_errors:
            self.ui.surname_error_label.setText(last_name_errors[0])
            self.ui.surname_error_label.setHidden(False)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = RegisterWindow()
    widget.show()

    app.exec()
