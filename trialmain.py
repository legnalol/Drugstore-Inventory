from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter
from PyQt5.QtGui import *
import sys, os, csv,pymysql
#login
class Login(QtWidgets.QMainWindow, QPushButton):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi('Login.ui', self)
        self.myOtherwindow = MyWindow()
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/Background.jpg);")
        self.pushButton.clicked.connect(self.on_open)
    def on_open(self):
        user = self.inputPass.text()
        pas  = self.inputUser.text()

        if user and pas == 'cuteako' :
            self.myOtherwindow.show()
            window.hide()
        else:
            QMessageBox.about(self, "ERROR", "Username/Password Is Incorrect")

#MAINWINDOW
class MyWindow(QtWidgets.QMainWindow, QPushButton):

    def __init__(self,*args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        uic.loadUi('Main.ui', self)
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/Background.jpg);")
        self.toolbaractions()

    def toolbaractions(self):#Toolbars clickable to access functions
        self.Refresh.triggered.connect(self.loaddata)
        self.Add_product.triggered.connect(self.insertdata)
        self.remove_product.triggered.connect(self.Removemember)
        self.edit_product.triggered.connect(self.Editmember)
        self.Search.triggered.connect(self.SearchMember)
    def loaddata(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.resizeRowsToContents()
        conn=pymysql.connect('localhost','Mark','termites','store')
        curr=conn.cursor()
        query=curr.execute("Select *from product")
        for i in curr:
            print(i)

        conn.close()
    def insertdata(self):
        dlg = InsertData()
        dlg.exec_()
    def Editmember(self):
        edt=EditDialog()
        edt.exec_()
    def Removemember(self):
        Dlt=DeleteDialog()
        Dlt.exec_()
    def SearchMember(self):
        search=SearchDialog()
        search.exec_()

#INSERT FUNCTION WINDOW
class InsertData(QDialog):
    def __init__(self, *args, **kwargs): #UI
        super(InsertData, self).__init__(*args, **kwargs)
        uic.loadUi('Add Product.ui', self)
        self.AddMembah.clicked.connect(self.addmember)
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/internal_medicine_zhanna_tsukerman.jpg);")


    def addmember(self): #function
        name  = self.Name.text()
        descr = self.Description.text()
        clas  = self.Classi.currentText()
        Qty   = self.spin.value()
        price = self.Price.text()
        pass

#DELETE FUNCTION WINDOW
class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):#UI
        super(DeleteDialog, self).__init__(*args, **kwargs)
        uic.loadUi('Delete Product.ui', self)
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/internal_medicine_zhanna_tsukerman.jpg);")
        self.DeleteMemba.clicked.connect(self.deletemember)
    def deletemember(self): #function

        delete=self.delete.text()
        pass

#EDIT FUNCTION WINDOW
class EditDialog(QDialog):
    def __init__(self, *args, **kwargs):#UI
        super(EditDialog, self).__init__(*args, **kwargs)
        uic.loadUi('Edit Product.ui', self)
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/internal_medicine_zhanna_tsukerman.jpg);")
        self.Update.clicked.connect(self.updatemember)

    def updatemember(self): #function
        id=int(self.id.text())
        name=self.Name.text()
        descri=self.descri.text()
        classi=self.classi.currentText()
        Qty=self.qty.value()
        price=int(self.price.text())
        pass

#SEARCH FUNCTION WINDOW
class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs): #UI
        super(SearchDialog, self).__init__(*args, **kwargs)
        uic.loadUi('Search Product.ui', self)
        self.graphicsView.setStyleSheet("background-image: url(Resourcess/internal_medicine_zhanna_tsukerman.jpg);")
        self.SearchMema.clicked.connect(self.searchMembers)

    def searchMembers(self): #function
        search = self.SearchLine.text()
        pass








if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
