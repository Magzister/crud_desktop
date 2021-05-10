from pyuic5_files.object_info import Ui_ObjectInfo
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from .edit_object_info import EditObjectInfoWindow


class ObjectInfoWindow(qtw.QWidget):

    edit_info_signal = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_ObjectInfo()
        self.ui.setupUi(self)

        self.access_token = None
        self.object_id = None
        self.object_name = None
        self.object_description = None
        self.edit_object_info_widget = None

        self.quit = qtw.QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)

        self.ui.change_button.clicked.connect(self.edit_object)
        self.ui.cancel_button.clicked.connect(self.close)

    def set_object_info(self, object_dict, access_token):
        self.object_id = object_dict['id']
        self.object_name = object_dict['name']
        self.object_description = object_dict['description']
        self.access_token = access_token
        self.update_labels()

    def edit_object(self):
        self.edit_object_info_widget = EditObjectInfoWindow()
        self.edit_object_info_widget.ok_signal.connect(self.ok_message)
        self.edit_object_info_widget.set_object_info(
            self.object_id,
            self.object_name,
            self.object_description,
            self.access_token
        )
        self.edit_object_info_widget.show()

    def ok_message(self, name, description):
        self.object_name = name
        self.object_description = description
        self.update_labels()
        self.edit_info_signal.emit()

    def update_labels(self):
        self.ui.name_label.setText(self.object_name)
        self.ui.description_text_browser.setText(self.object_description)

    def closeEvent(self, event):
        if self.edit_object_info_widget:
            self.edit_object_info_widget.close()
        event.accept()


if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = ObjectInfoWindow()
    widget.show()

    app.exec()
