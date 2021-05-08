# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Authentication(object):
    def setupUi(self, Authentication):
        Authentication.setObjectName("Authentication")
        Authentication.resize(289, 235)
        self.formLayout = QtWidgets.QFormLayout(Authentication)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Authentication)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(Authentication)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.username_edit = QtWidgets.QLineEdit(Authentication)
        self.username_edit.setObjectName("username_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username_edit)
        self.label_3 = QtWidgets.QLabel(Authentication)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.password_edit = QtWidgets.QLineEdit(Authentication)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_edit)
        self.login_button = QtWidgets.QPushButton(Authentication)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.login_button)
        self.registration_button = QtWidgets.QPushButton(Authentication)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.registration_button.setFont(font)
        self.registration_button.setObjectName("registration_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.registration_button)
        self.username_error_label = QtWidgets.QLabel(Authentication)
        self.username_error_label.setObjectName("username_error_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.username_error_label)
        self.password_error_label = QtWidgets.QLabel(Authentication)
        self.password_error_label.setEnabled(True)
        self.password_error_label.setObjectName("password_error_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.password_error_label)

        self.retranslateUi(Authentication)
        QtCore.QMetaObject.connectSlotsByName(Authentication)

    def retranslateUi(self, Authentication):
        _translate = QtCore.QCoreApplication.translate
        Authentication.setWindowTitle(_translate("Authentication", "Authentication"))
        self.label.setText(_translate("Authentication", "Login"))
        self.label_2.setText(_translate("Authentication", "Username"))
        self.label_3.setText(_translate("Authentication", "Password"))
        self.login_button.setText(_translate("Authentication", "Login"))
        self.registration_button.setText(_translate("Authentication", "Registration"))
        self.username_error_label.setText(_translate("Authentication", "123"))
        self.password_error_label.setText(_translate("Authentication", "123"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Authentication = QtWidgets.QWidget()
    ui = Ui_Authentication()
    ui.setupUi(Authentication)
    Authentication.show()
    sys.exit(app.exec_())
