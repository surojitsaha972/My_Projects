from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
# from loginPage import *

class Ui_changePa(object):
    def __init__(self,e):
        self.mail = e
    def setupUi(self, changePa):
        changePa.setObjectName("changePa")
        changePa.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(changePa)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.oldPa = QtWidgets.QLineEdit(self.frame_2)
        self.oldPa.setObjectName("oldPa")
        self.horizontalLayout.addWidget(self.oldPa)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.newPa = QtWidgets.QLineEdit(self.frame_3)
        self.newPa.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPa.setObjectName("newPa")
        self.horizontalLayout_2.addWidget(self.newPa)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.reNePa = QtWidgets.QLineEdit(self.frame_4)
        self.reNePa.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reNePa.setObjectName("reNePa")
        self.horizontalLayout_3.addWidget(self.reNePa)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change = QtWidgets.QPushButton(self.frame_5)
        self.change.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change.setObjectName("change")
        self.horizontalLayout_4.addWidget(self.change)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        changePa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changePa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        changePa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changePa)
        self.statusbar.setObjectName("statusbar")
        changePa.setStatusBar(self.statusbar)

        self.retranslateUi(changePa)
        QtCore.QMetaObject.connectSlotsByName(changePa)

    def retranslateUi(self, changePa):
        _translate = QtCore.QCoreApplication.translate
        changePa.setWindowTitle(_translate("changePa", "Change Password"))
        self.label.setText(_translate("changePa", "Change Password"))
        self.label_2.setText(_translate("changePa", "Old Password"))
        self.label_3.setText(_translate("changePa", "New Password"))
        self.label_4.setText(_translate("changePa", "Reenter the new"))
        self.label_5.setText(_translate("changePa", "password"))
        self.change.setText(_translate("changePa", "Change"))

    def chng(self):
        oldPass = self.oldPa.text()
        newPass = self.newPa.text()
        # oldPass = self.oldPa.text()
        rePass = self.reNePa.text()
        if oldPass == "" or newPass == "" or rePass == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Fields cann't be empty")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        else:
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Critical)
            # msg.setText("Ok")
            # msg.setWindowTitle("Warning")
            # msg.show()
            # msg.exec_()
            con = sqlite3.connect("projectDB.db")
            cur = con.cursor()
            q = "select Password from admin where email = ?"
            cur.execute(q,(self.mail,))
            res = cur.fetchall()
            if oldPass != res[0][0]:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Original password mismatch")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
                # print(self.mail)
            if oldPass == res[0][0]:
                if newPass != rePass:
                    # print(newPass,rePass)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("New and Re-enter password not match")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()
                else:
                    cu1 = con.cursor()
                    q = "update Admin set Password = ? where Email = ?"
                    cur.execute(q,(newPass,self.mail))

                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Password Changed")
                    msg.setWindowTitle("Information")
                    msg.show()
                    msg.exec_()

                    # self.change.clicked.connect(changePa.close)
                    # login = QtWidgets.QMainWindow()
                    # ui = Ui_login()
                    # ui.setupUi(login)
                    # login.show()
            con.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changePa = QtWidgets.QMainWindow()
    ui = Ui_changePa()
    ui.setupUi(changePa)
    changePa.show()
    sys.exit(app.exec_())
