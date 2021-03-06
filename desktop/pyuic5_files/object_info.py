# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\object_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ObjectInfo(object):
    def setupUi(self, ObjectInfo):
        ObjectInfo.setObjectName("ObjectInfo")
        ObjectInfo.resize(414, 651)
        self.description_text_browser = QtWidgets.QTextBrowser(ObjectInfo)
        self.description_text_browser.setGeometry(QtCore.QRect(10, 90, 391, 192))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.description_text_browser.setFont(font)
        self.description_text_browser.setObjectName("description_text_browser")
        self.name_label = QtWidgets.QLabel(ObjectInfo)
        self.name_label.setGeometry(QtCore.QRect(10, 30, 381, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.label = QtWidgets.QLabel(ObjectInfo)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ObjectInfo)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.change_button = QtWidgets.QPushButton(ObjectInfo)
        self.change_button.setGeometry(QtCore.QRect(10, 290, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.change_button.setFont(font)
        self.change_button.setObjectName("change_button")
        self.cancel_button = QtWidgets.QPushButton(ObjectInfo)
        self.cancel_button.setGeometry(QtCore.QRect(310, 610, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.access_list_widget = QtWidgets.QListWidget(ObjectInfo)
        self.access_list_widget.setGeometry(QtCore.QRect(10, 360, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.access_list_widget.setFont(font)
        self.access_list_widget.setObjectName("access_list_widget")
        self.invite_button = QtWidgets.QPushButton(ObjectInfo)
        self.invite_button.setGeometry(QtCore.QRect(110, 610, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.invite_button.setFont(font)
        self.invite_button.setObjectName("invite_button")
        self.delete_button = QtWidgets.QPushButton(ObjectInfo)
        self.delete_button.setGeometry(QtCore.QRect(210, 610, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.label_3 = QtWidgets.QLabel(ObjectInfo)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.update_button = QtWidgets.QPushButton(ObjectInfo)
        self.update_button.setGeometry(QtCore.QRect(10, 610, 93, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")

        self.retranslateUi(ObjectInfo)
        QtCore.QMetaObject.connectSlotsByName(ObjectInfo)

    def retranslateUi(self, ObjectInfo):
        _translate = QtCore.QCoreApplication.translate
        ObjectInfo.setWindowTitle(_translate("ObjectInfo", "Info"))
        self.description_text_browser.setHtml(_translate("ObjectInfo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">description</span></p></body></html>"))
        self.name_label.setText(_translate("ObjectInfo", "Name"))
        self.label.setText(_translate("ObjectInfo", "Object name:"))
        self.label_2.setText(_translate("ObjectInfo", "Object description:"))
        self.change_button.setText(_translate("ObjectInfo", "Change"))
        self.cancel_button.setText(_translate("ObjectInfo", "Cancel"))
        self.invite_button.setText(_translate("ObjectInfo", "Invite"))
        self.delete_button.setText(_translate("ObjectInfo", "Delete"))
        self.label_3.setText(_translate("ObjectInfo", "Accesses"))
        self.update_button.setText(_translate("ObjectInfo", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ObjectInfo = QtWidgets.QWidget()
    ui = Ui_ObjectInfo()
    ui.setupUi(ObjectInfo)
    ObjectInfo.show()
    sys.exit(app.exec_())
