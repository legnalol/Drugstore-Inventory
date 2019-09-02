# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertcust.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.CustIDLabel = QtWidgets.QLabel(Dialog)
        self.CustIDLabel.setGeometry(QtCore.QRect(40, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CustIDLabel.setFont(font)
        self.CustIDLabel.setObjectName("CustIDLabel")
        self.CustFNLAbel = QtWidgets.QLabel(Dialog)
        self.CustFNLAbel.setGeometry(QtCore.QRect(40, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CustFNLAbel.setFont(font)
        self.CustFNLAbel.setObjectName("CustFNLAbel")
        self.CustLNLabel = QtWidgets.QLabel(Dialog)
        self.CustLNLabel.setGeometry(QtCore.QRect(40, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CustLNLabel.setFont(font)
        self.CustLNLabel.setObjectName("CustLNLabel")
        self.CustIdText = QtWidgets.QLineEdit(Dialog)
        self.CustIdText.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.CustIdText.setObjectName("CustIdText")
        self.CustFNText = QtWidgets.QLineEdit(Dialog)
        self.CustFNText.setGeometry(QtCore.QRect(120, 120, 161, 20))
        self.CustFNText.setObjectName("CustFNText")
        self.CustLNText = QtWidgets.QLineEdit(Dialog)
        self.CustLNText.setGeometry(QtCore.QRect(120, 180, 161, 21))
        self.CustLNText.setObjectName("CustLNText")
        self.CustTitle = QtWidgets.QLabel(Dialog)
        self.CustTitle.setGeometry(QtCore.QRect(130, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(14)
        self.CustTitle.setFont(font)
        self.CustTitle.setObjectName("CustTitle")
        self.custokbutton = QtWidgets.QPushButton(Dialog)
        self.custokbutton.setGeometry(QtCore.QRect(110, 250, 75, 23))
        self.custokbutton.setObjectName("custokbutton")
        self.custcancelbutton = QtWidgets.QPushButton(Dialog)
        self.custcancelbutton.setGeometry(QtCore.QRect(210, 250, 75, 23))
        self.custcancelbutton.setObjectName("custcancelbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.CustIDLabel.setText(_translate("Dialog", "CustomerID"))
        self.CustFNLAbel.setText(_translate("Dialog", "First Name"))
        self.CustLNLabel.setText(_translate("Dialog", "Last Name"))
        self.CustTitle.setText(_translate("Dialog", "CUSTOMERS"))
        self.custokbutton.setText(_translate("Dialog", "OK"))
        self.custcancelbutton.setText(_translate("Dialog", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
