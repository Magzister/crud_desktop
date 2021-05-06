from pyuic5_files.object_list import Ui_ObjectList
from PyQt5 import QtWidgets as qtw
from models.object_list_model import ObjectList

import requests
import device

GET_OBJECT_LIST_URL = 'http://localhost:8000/objects/'
GET_OBJECT_DETAIL_URL = 'http://localhost:8000/objects/{id}'


class ObjectsWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ObjectList()
        self.ui.setupUi(self)
        self.ui.object_list_widget.itemDoubleClicked.connect(self.object_double_clicked)
        self.ui.update_btn.clicked.connect(self.update_object_list)

        self.object_list = ObjectList()
        self.update_object_list()

    def update_object_list(self):
        self.ui.object_list_widget.clear()
        response = requests.get(GET_OBJECT_LIST_URL)
        if response:
            object_list = response.json()
            self.object_list.set_object_list(object_list)
            for obj in object_list:
                self.ui.object_list_widget.addItem(obj['name'])

    def update_camera_list(self):
        pass

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


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = ObjectsWindow()
    widget.show()

    app.exec()
