from pyuic5_files.edit_object_info import Ui_EditObjectInfo
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import requests


OBJECT_DETAIL_URL = 'http://localhost:8000/objects/{id}/'


class EditObjectInfoWindow(qtw.QWidget):

    ok_signal = qtc.pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_EditObjectInfo()
        self.ui.setupUi(self)

        self.object_id = None
        self.object_name = None
        self.object_description = None
        self.access_token = None

        self.ui.ok_cancel_button_box.accepted.connect(self.update_object_info)
        self.ui.ok_cancel_button_box.rejected.connect(self.close)

    def set_object_info(self, id, name, description, access_token):
        self.object_id = id
        self.object_name = name
        self.object_description = description
        self.access_token = access_token
        self.ui.name_edit.setText(name)
        self.ui.description_edit.setText(description)

    def update_object_info(self):
        new_name = self.ui.name_edit.text()
        new_description = self.ui.description_edit.toPlainText()
        if self.object_name == new_name and self.object_description == new_description:
            self.close()

        url = OBJECT_DETAIL_URL.format(
            id=self.object_id
        )
        data = {
            'name': new_name,
            'description': new_description
        }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.put(url=url, data=data, headers=headers)
        if response.status_code == 200:
            qtw.QMessageBox.information(self, 'Success', 'Object updated!')
            self.ok_signal.emit(new_name, new_description)
            self.close()
        if response.status_code == 400:
            qtw.QMessageBox.information(self, 'Failure', response.text)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = EditObjectInfoWindow()
    widget.show()

    app.exec()
