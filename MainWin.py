# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/S.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.WelcomeScreen = QtWidgets.QLabel(self.centralwidget)
        self.WelcomeScreen.setGeometry(QtCore.QRect(160, 0, 651, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.WelcomeScreen.setFont(font)
        self.WelcomeScreen.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeScreen.setObjectName("WelcomeScreen")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 50, 671, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(570, 550, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.time.setFont(font)
        self.time.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time.setFrameShadow(QtWidgets.QFrame.Plain)
        self.time.setText("")
        self.time.setObjectName("time")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 80, 651, 441))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-10, -10, 971, 591))
        self.graphicsView.setStyleSheet("background-image: url(:/Backgrounds/Background.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 220, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 320, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.graphicsView.raise_()
        self.WelcomeScreen.raise_()
        self.line.raise_()
        self.tableWidget.raise_()
        self.time.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCash = QtWidgets.QMenu(self.menubar)
        self.menuCash.setObjectName("menuCash")
        self.menuSettings_2 = QtWidgets.QMenu(self.menubar)
        self.menuSettings_2.setObjectName("menuSettings_2")
        self.menuFile_2 = QtWidgets.QMenu(self.menubar)
        self.menuFile_2.setObjectName("menuFile_2")
        MainWindow.setMenuBar(self.menubar)
        self.Add_product = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Resources/user-add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Add_product.setIcon(icon1)
        self.Add_product.setObjectName("Add_product")
        self.edit_product = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Resources/Male-user-edit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_product.setIcon(icon2)
        self.edit_product.setObjectName("edit_product")
        self.remove_product = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Resources/user-remove-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_product.setIcon(icon3)
        self.remove_product.setObjectName("remove_product")
        self.actionEdit_User = QtWidgets.QAction(MainWindow)
        self.actionEdit_User.setObjectName("actionEdit_User")
        self.User = QtWidgets.QAction(MainWindow)
        self.User.setObjectName("User")
        self.Cooperative_Withdrawals = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Resources/donation-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Cooperative_Withdrawals.setIcon(icon4)
        self.Cooperative_Withdrawals.setObjectName("Cooperative_Withdrawals")
        self.Member_deposits = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Resources/dep.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Member_deposits.setIcon(icon5)
        self.Member_deposits.setObjectName("Member_deposits")
        self.Print = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Resources/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Print.setIcon(icon6)
        self.Print.setObjectName("Print")
        self.Member_Withdrawals = QtWidgets.QAction(MainWindow)
        self.Member_Withdrawals.setIcon(icon4)
        self.Member_Withdrawals.setObjectName("Member_Withdrawals")
        self.Cooperative_deposits = QtWidgets.QAction(MainWindow)
        self.Cooperative_deposits.setIcon(icon5)
        self.Cooperative_deposits.setObjectName("Cooperative_deposits")
        self.Developer = QtWidgets.QAction(MainWindow)
        self.Developer.setObjectName("Developer")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.Editofficials = QtWidgets.QAction(MainWindow)
        self.Editofficials.setObjectName("Editofficials")
        self.Search = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Resources/01-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search.setIcon(icon7)
        self.Search.setObjectName("Search")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Resources/refresh_playback_back_again_control_icon_multimedia_blue_video-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon8)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionUser = QtWidgets.QAction(MainWindow)
        self.actionUser.setObjectName("actionUser")
        self.Refresh = QtWidgets.QAction(MainWindow)
        self.Refresh.setObjectName("Refresh")
        self.menuFile.addAction(self.Add_product)
        self.menuFile.addAction(self.remove_product)
        self.menuFile.addAction(self.edit_product)
        self.menuFile.addAction(self.Search)
        self.menuFile.addAction(self.Refresh)
        self.menuCash.addAction(self.Member_deposits)
        self.menuCash.addSeparator()
        self.menuSettings_2.addAction(self.actionAbout)
        self.menuSettings_2.addAction(self.actionUser)
        self.menuFile_2.addAction(self.Print)
        self.menuFile_2.addAction(self.Exit)
        self.menubar.addAction(self.menuFile_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCash.menuAction())
        self.menubar.addAction(self.menuSettings_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inventory System"))
        self.WelcomeScreen.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">CLAIRE\'S DRUGSTORE</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Unit Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Classification"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Quantity"))
        self.menuFile.setTitle(_translate("MainWindow", "Product"))
        self.menuCash.setTitle(_translate("MainWindow", "Cash Deposits"))
        self.menuSettings_2.setTitle(_translate("MainWindow", "Settings"))
        self.menuFile_2.setTitle(_translate("MainWindow", "File"))
        self.Add_product.setText(_translate("MainWindow", "Add Product"))
        self.Add_product.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.edit_product.setText(_translate("MainWindow", "Edit Product"))
        self.edit_product.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.remove_product.setText(_translate("MainWindow", "Delete Product"))
        self.remove_product.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionEdit_User.setText(_translate("MainWindow", "Edit User"))
        self.User.setText(_translate("MainWindow", "User"))
        self.Cooperative_Withdrawals.setText(_translate("MainWindow", "Cooperative Expenses"))
        self.Member_deposits.setText(_translate("MainWindow", "Sales Report"))
        self.Print.setText(_translate("MainWindow", "Print"))
        self.Print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.Member_Withdrawals.setText(_translate("MainWindow", "Member Withdrawals"))
        self.Cooperative_deposits.setText(_translate("MainWindow", "Cooperative Income"))
        self.Developer.setText(_translate("MainWindow", "Developer"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.Editofficials.setText(_translate("MainWindow", "Edit Officials"))
        self.Search.setText(_translate("MainWindow", "Search Product"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "F5"))
        self.actionUser.setText(_translate("MainWindow", "User"))
        self.Refresh.setText(_translate("MainWindow", "Refresh"))
        self.Refresh.setShortcut(_translate("MainWindow", "F5"))
import BG_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
