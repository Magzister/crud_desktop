from pyuic5_files.object_list import Ui_ObjectList
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from models.object_list_model import ObjectList
from models.device_process import DeviceProcess
from .object_info import ObjectInfoWindow
from .create_object import CreateObjectWindow

import requests
import threading
import cv2


GET_OBJECT_LIST_URL = 'http://localhost:8000/objects/'
OBJECT_DETAIL_URL = 'http://localhost:8000/objects/{id}/'


class ObjectsWindow(qtw.QWidget):

    logout_signal = qtc.pyqtSignal()
    object_info_signal = qtc.pyqtSignal(str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ObjectList()
        self.ui.setupUi(self)
        self.ui.object_list_widget.itemDoubleClicked.connect(self.object_double_clicked)
        self.ui.update_btn.clicked.connect(self.update_object_list)
        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.link_btn.clicked.connect(self.link_object)
        self.ui.delete_button.clicked.connect(self.delete_item)
        self.ui.add_button.clicked.connect(self.add_item)

        self.quit = qtw.QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)

        self.username = None
        self.access_token = None
        self.refresh_token = None
        self.object_info_widget = None
        self.create_object_window = None

        self.device_list = [cv2.VideoCapture(0)]

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
        ind = self.ui.object_list_widget.indexFromItem(item).row()
        object_dict = self.object_list.get_list_item(ind)
        self.object_info_widget = ObjectInfoWindow()
        self.object_info_widget.edit_info_signal.connect(self.update_object_list)
        self.object_info_widget.set_object_info(object_dict, self.access_token)
        self.object_info_widget.show()

    def set_login_data(self, username, access_token, refresh_token):
        self.username = username
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.ui.username_label.setText(self.username)
        self.update_object_list()

    def logout(self):
        self.logout_signal.emit()

    def closeEvent(self, event):
        if self.object_info_widget:
            self.object_info_widget.close()
        if self.create_object_window:
            self.create_object_window.close()
        event.accept()

    def delete_item(self):
        selected_indexes = self.ui.object_list_widget.selectedIndexes()
        if selected_indexes:
            object_dict = self.object_list.get_list_item(selected_indexes[0].row())
            headers = {'Authorization': f'Bearer {self.access_token}'}
            url = OBJECT_DETAIL_URL.format(
                id=object_dict['id']
            )
            response = requests.delete(url=url, headers=headers)
            if response.status_code == 204:
                self.update_object_list()
            else:
                qtw.QMessageBox.information(self, 'Failure', response.text)

    def add_item(self):
        self.create_object_window = CreateObjectWindow()
        self.create_object_window.ok_signal.connect(self.update_object_list)
        self.create_object_window.set_token(self.access_token)
        self.create_object_window.show()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = ObjectsWindow()
    widget.show()

    app.exec()
