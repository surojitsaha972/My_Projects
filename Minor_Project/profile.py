# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from time import monotonic
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_pro(object):
    def __init__(self,e,n,m):
        self.mail = e
        self.n = n
        self.m = m
    def setupUi(self, pro):
        pro.setObjectName("pro")
        pro.resize(800, 600)
        pro.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(pro)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.email = QtWidgets.QLabel(self.frame_2)
        self.email.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setStyleSheet("color: rgb(0, 0, 255);")
        self.email.setObjectName("email")
        self.horizontalLayout_2.addWidget(self.email)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.name = QtWidgets.QLineEdit(self.frame_3)
        self.name.setMinimumSize(QtCore.QSize(250, 0))
        self.name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.name.setObjectName("name")
        self.horizontalLayout_3.addWidget(self.name)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.mobile = QtWidgets.QLineEdit(self.frame_4)
        self.mobile.setMinimumSize(QtCore.QSize(200, 0))
        self.mobile.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mobile.setObjectName("mobile")
        self.horizontalLayout_4.addWidget(self.mobile)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edit = QtWidgets.QPushButton(self.frame_5)
        self.edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit.setObjectName("edit")
        self.horizontalLayout_5.addWidget(self.edit)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        pro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        pro.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pro)
        self.statusbar.setObjectName("statusbar")
        pro.setStatusBar(self.statusbar)

        self.retranslateUi(pro)
        QtCore.QMetaObject.connectSlotsByName(pro)

        self.email.setText(self.mail)
        self.name.setText(self.n)
        self.mobile.setText(self.m)
        self.edit.clicked.connect(self.ed)
        self.edit.clicked.connect(pro.close)

    def retranslateUi(self, pro):
        _translate = QtCore.QCoreApplication.translate
        pro.setWindowTitle(_translate("pro", "Profile"))
        self.label.setText(_translate("pro", "Profile"))
        self.label_9.setText(_translate("pro", "Email"))
        self.email.setText(_translate("pro", "e"))
        self.label_7.setText(_translate("pro", "Name"))
        self.label_8.setText(_translate("pro", "Mobile No"))
        self.edit.setText(_translate("pro", "Edit"))

    def ed(self):
        Name = self.name.text()
        Mobile = self.mobile.text()
        # email = "xyz@gmail.com"
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()

        q = "update admin set Name = ?, MobileNo = ? where email = ?"
        cur.execute(q,(Name,Mobile,self.mail))
        con.commit()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Update succesfull")
        msg.setWindowTitle("Edit profile")
        msg.show()
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pro = QtWidgets.QMainWindow()
    ui = Ui_pro()
    ui.setupUi(pro)
    pro.show()
    sys.exit(app.exec_())
