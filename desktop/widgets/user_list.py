from pyuic5_files.user_list import Ui_UserList
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from models.object_list_model import ObjectList

import requests


USER_LIST_URL = 'http://localhost:8000/users/no-access/{id}'
INVITE_URL = 'http://localhost:8000/users/{user_id}/invite/{object_id}'


class UserListWindow(qtw.QWidget):

    registration_signal = qtc.pyqtSignal(str)
    cancel_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_UserList()
        self.ui.setupUi(self)

        self.object_id = None
        self.access_token = None
        self.users_list = ObjectList()

        self.ui.update_button.clicked.connect(self.update_user_list)
        self.ui.invite_button.clicked.connect(self.invite)
        self.ui.cancel_button.clicked.connect(self.close)

    def set_object_info(self, object_id, access_token):
        self.object_id = object_id
        self.access_token = access_token
        self.update_user_list()

    def update_user_list(self):
        self.ui.user_list_widget.clear()
        url = USER_LIST_URL.format(
            id=self.object_id
        )
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            users_list = response.json()
            self.users_list.set_object_list(users_list)
            for user in users_list:
                item = '{name} {surname} ({username})'
                self.ui.user_list_widget.addItem(
                    item.format(
                        name=user['first_name'],
                        surname=user['last_name'],
                        username=user['username']
                    )
                )

    def invite(self):
        selected_indexes = self.ui.user_list_widget.selectedIndexes()
        if selected_indexes:
            user_dict = self.users_list.get_list_item(selected_indexes[0].row())
            headers = {'Authorization': f'Bearer {self.access_token}'}
            url = INVITE_URL.format(
                user_id=user_dict['id'],
                object_id=self.object_id
            )
            response = requests.post(url=url, headers=headers)
            if response.status_code == 200:
                username = user_dict['username']
                qtw.QMessageBox.information(self, 'Success', f'{username} invited!')
                self.update_user_list()
            else:
                qtw.QMessageBox.information(self, 'Failure', response.text)


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = UserListWindow()
    widget.show()

    app.exec()
