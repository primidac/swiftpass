# Primidac Codes

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sqlite3 as db

# this code is shaky

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 250)
        MainWindow.setMaximumSize(QtCore.QSize(320, 250))
        MainWindow.setSizeIncrement(QtCore.QSize(320, 250))
        MainWindow.setBaseSize(QtCore.QSize(320, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(127, 10, 71, 20))
        self.label.setStyleSheet("font: 18 10pt \"Ubuntu Thin\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 50, 320, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(320, 250))
        self.lineEdit.setSizeIncrement(QtCore.QSize(320, 250))
        self.lineEdit.setBaseSize(QtCore.QSize(320, 250))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 90, 321, 71))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 160, 88, 34))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreate_Account = QtWidgets.QAction(MainWindow)
        self.actionCreate_Account.setObjectName("actionCreate_Account")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionCreate_Account)
        self.menuMenu.addAction(self.actionLogin)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        # testing

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SwiftPass"))
        self.label.setText(_translate("MainWindow", " Swift Pass"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter Name of Account for password. Eg. Twitter(x)"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Account Name"))
        self.textEdit.setToolTip(_translate("MainWindow", "Your SwiftPass Appears Here and ge copied to your clipboard"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Your SwiftPass"))
        self.pushButton.setText(_translate("MainWindow", "MySwiftPass"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCreate_Account.setText(_translate("MainWindow", "Create Account"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
