from pyuic5_files.create_object import Ui_CreateObject
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import requests


OBJECTS_URL = 'http://localhost:8000/objects/'


class CreateObjectWindow(qtw.QWidget):

    ok_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_CreateObject()
        self.ui.setupUi(self)

        self.access_token = None

        self.ui.ok_cancel_button_box.accepted.connect(self.create_object)
        self.ui.ok_cancel_button_box.rejected.connect(self.close)

    def create_object(self):
        name = self.ui.name_edit.text()
        description = self.ui.description_edit.toPlainText()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'name': name,
            'description': description
        }
        response = requests.post(url=OBJECTS_URL, data=data, headers=headers)
        if response.status_code == 201:
            qtw.QMessageBox.information(self, 'Success', 'Object created!')
            self.ok_signal.emit()
            self.close()
        else:
            qtw.QMessageBox.information(self, 'Failure', response.text)

    def set_token(self, token):
        self.access_token = token


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = CreateObjectWindow()
    widget.show()

    app.exec()
