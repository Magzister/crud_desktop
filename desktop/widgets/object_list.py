from pyuic5_files.object_list import Ui_ObjectList
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from models.object_list_model import ObjectList
from models.device_process import DeviceProcess

import requests
import threading
import cv2


GET_OBJECT_LIST_URL = 'http://localhost:8000/objects/'
GET_OBJECT_DETAIL_URL = 'http://localhost:8000/objects/{id}'


class ObjectsWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ObjectList()
        self.ui.setupUi(self)
        self.ui.object_list_widget.itemDoubleClicked.connect(self.object_double_clicked)
        self.ui.update_btn.clicked.connect(self.update_object_list)
        self.ui.link_btn.clicked.connect(self.link_object)

        self.username = ''
        self.access_token = ''
        self.refresh_token = ''

        self.device_list = [cv2.VideoCapture(0, cv2.CAP_DSHOW)]

        self.object_list = ObjectList()

    def link_object(self):
        object_ind = self.ui.object_list_widget.selectedIndexes()[0].row()
        element = self.object_list.get_list_item(object_ind)
        id = element['id']
        name = element['name']
        self.create_process(id, name)

    def create_process(self, object_id, object_name):
        device_process = DeviceProcess(object_id, object_name, self.device_list[0])
        t = threading.Thread(target=device_process.run)
        t.start()

    def update_object_list(self):
        self.ui.object_list_widget.clear()
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.get(GET_OBJECT_LIST_URL, headers=headers)
        if response.status_code == 200:
            object_list = response.json()
            self.object_list.set_object_list(object_list)
            for obj in object_list:
                self.ui.object_list_widget.addItem(obj['name'])

    def object_double_clicked(self, item):
        text = 'id: {id}\n' + 'name: {name}\n' + 'description: {description}'
        ind = self.ui.object_list_widget.indexFromItem(item).row()
        element = self.object_list.get_list_item(ind)
        qtw.QMessageBox.information(
            self,
            "Object Details",
            text.format(
                id=element['id'],
                name=element['name'],
                description=element['description']
            )
        )

    @qtc.pyqtSlot(str, str, str)
    def login_message(self, username, access_token, refresh_token):
        self.username = username
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.ui.username_label.setText(self.username)
        # self.update_object_list()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = ObjectsWindow()
    widget.show()

    app.exec()
