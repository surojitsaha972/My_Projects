# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'call2Pages.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from bookRequest import *
from bookRequestClosed import *
from datetime import datetime

class Ui_callPage(object):
    def setupUi(self, callPage):
        callPage.setObjectName("callPage")
        callPage.resize(0, 0)
        self.centralwidget = QtWidgets.QWidget(callPage)
        self.centralwidget.setObjectName("centralwidget")
        callPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(callPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.menubar.setObjectName("menubar")
        callPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(callPage)
        self.statusbar.setObjectName("statusbar")
        callPage.setStatusBar(self.statusbar)

        self.retranslateUi(callPage)
        QtCore.QMetaObject.connectSlotsByName(callPage)
        # self.callPage
        self.call()
        # callPage.close()

    def retranslateUi(self, callPage):
        _translate = QtCore.QCoreApplication.translate
        callPage.setWindowTitle(_translate("callPage", "MainWindow"))

    def call(self):
        curTime = datetime.now().time()
        closingTime = datetime.strptime("13:30:00", "%H:%M:%S").time()
        openTime = datetime.strptime("10:00:00", "%H:%M:%S").time()
        
        if curTime < closingTime and curTime >= openTime:
            self.bookReq = QtWidgets.QMainWindow()
            self.ui = Ui_bookReq()
            self.ui.setupUi(self.bookReq)
            self.bookReq.show()
        
        else:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    callPage = QtWidgets.QMainWindow()
    ui = Ui_callPage()
    ui.setupUi(callPage)
    callPage.show()
    # app.quit()
    sys.exit(app.exec_())
