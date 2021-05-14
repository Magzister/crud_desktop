from pyuic5_files.invite_list import Ui_InvitesList
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from models.object_list_model import ObjectList

import requests


ACCESS_OFFERS_URL = 'http://localhost:8000/accesses/offers/'
ACCEPT_OFFER_URL = 'http://localhost:8000/accesses/accept/{id}'
REJECT_OFFER_URL = 'http://localhost:8000/accesses/offers/{id}'


class InviteListWindow(qtw.QWidget):

    registration_signal = qtc.pyqtSignal(str)
    cancel_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_InvitesList()
        self.ui.setupUi(self)

        self.access_token = None
        self.invites_list = ObjectList()

        self.ui.reject_button.clicked.connect(self.reject)
        self.ui.accept_button.clicked.connect(self.accept)
        self.ui.update_button.clicked.connect(self.update_invite_list)
        self.ui.cancel_button.clicked.connect(self.close)

    def accept(self):
        selected_indexes = self.ui.invite_list_wiget.selectedIndexes()
        if selected_indexes:
            invite_dict = self.invites_list.get_list_item(selected_indexes[0].row())
            url = ACCEPT_OFFER_URL.format(
                id=invite_dict['id']
            )
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.post(url=url, headers=headers)
            if response.status_code == 200:
                qtw.QMessageBox.information(self, 'Success', 'Invite accepted.')
                self.update_invite_list()
            else:
                qtw.QMessageBox.information(self, 'Failure', response.text)

    def reject(self):
        selected_indexes = self.ui.invite_list_wiget.selectedIndexes()
        if selected_indexes:
            invite_dict = self.invites_list.get_list_item(selected_indexes[0].row())
            url = REJECT_OFFER_URL.format(
                id=invite_dict['id']
            )
            headers = {'Authorization': f'Bearer {self.access_token}'}
            response = requests.delete(url=url, headers=headers)
            if response.status_code == 204:
                qtw.QMessageBox.information(self, 'Success', 'Invite rejected.')
            else:
                qtw.QMessageBox.information(self, 'Failure', response.text)

    def update_invite_list(self):
        self.ui.invite_list_wiget.clear()
        url = ACCESS_OFFERS_URL
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            access_list = response.json()
            self.invites_list.set_object_list(access_list)
            for access in access_list:
                object = access['object']
                item = '{object_name} ({owner_username})'
                self.ui.invite_list_wiget.addItem(
                    item.format(
                        object_name=object['name'],
                        owner_username=object['owner']['username']
                    )
                )

    def set_object_info(self, access_token):
        self.access_token = access_token
        self.update_invite_list()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = InviteListWindow()
    widget.show()

    app.exec()
