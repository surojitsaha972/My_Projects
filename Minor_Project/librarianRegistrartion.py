from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import re

class Ui_librarian_registration(object):
    def setupUi(self, librarian_registration):
        librarian_registration.setObjectName("librarian_registration")
        librarian_registration.resize(881, 553)
        self.centralwidget = QtWidgets.QWidget(librarian_registration)
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
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.name = QtWidgets.QLineEdit(self.frame_2)
        self.name.setMinimumSize(QtCore.QSize(200, 0))
        self.name.setMaximumSize(QtCore.QSize(400, 30))
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.mobile = QtWidgets.QLineEdit(self.frame_3)
        self.mobile.setMinimumSize(QtCore.QSize(200, 0))
        self.mobile.setMaximumSize(QtCore.QSize(300, 30))
        self.mobile.setObjectName("mobile")
        self.horizontalLayout_2.addWidget(self.mobile)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.email = QtWidgets.QLineEdit(self.frame_4)
        self.email.setMinimumSize(QtCore.QSize(200, 0))
        self.email.setMaximumSize(QtCore.QSize(300, 30))
        self.email.setObjectName("email")
        self.horizontalLayout_3.addWidget(self.email)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMinimumSize(QtCore.QSize(170, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.frame_5)
        self.password.setMinimumSize(QtCore.QSize(200, 0))
        self.password.setMaximumSize(QtCore.QSize(300, 30))
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.repass = QtWidgets.QLineEdit(self.frame_6)
        self.repass.setMinimumSize(QtCore.QSize(200, 0))
        self.repass.setMaximumSize(QtCore.QSize(300, 30))
        self.repass.setObjectName("repass")
        self.horizontalLayout_5.addWidget(self.repass)
        self.verticalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.reg = QtWidgets.QPushButton(self.frame_7)
        self.reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reg.setObjectName("reg")
        self.horizontalLayout_6.addWidget(self.reg)
        self.verticalLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        librarian_registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(librarian_registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        librarian_registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(librarian_registration)
        self.statusbar.setObjectName("statusbar")
        librarian_registration.setStatusBar(self.statusbar)

        self.retranslateUi(librarian_registration)
        QtCore.QMetaObject.connectSlotsByName(librarian_registration)
        
        self.reg.clicked.connect(self.registration)

    def retranslateUi(self, librarian_registration):
        _translate = QtCore.QCoreApplication.translate
        librarian_registration.setWindowTitle(_translate("librarian_registration", "Staff Registration"))
        self.label.setText(_translate("librarian_registration", "Staff registration"))
        self.label_2.setText(_translate("librarian_registration", "Name"))
        self.label_5.setText(_translate("librarian_registration", "Mobile No"))
        self.label_4.setText(_translate("librarian_registration", "Email"))
        self.label_3.setText(_translate("librarian_registration", "Password"))
        self.label_6.setText(_translate("librarian_registration", "Re-enter Password"))
        self.reg.setText(_translate("librarian_registration", "Register"))

    def registration(self):
        e = self.email.text()
        p = self.password.text()
        rp = self.repass.text()
        m = self.mobile.text()
        n = self.name.text()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, e):
            emailValid = 1;
        else:
            emailValid = 0;
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()

        # if e=="" or m=="" or p=="" or n=="":
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("Fields cann't be empty")
        #     msg.setWindowTitle("Warning")
        #     msg.show()
        #     msg.exec_()

        if n=="": 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Name field cann't be empty")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        
        elif m=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Moblie number field cann't be empty")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        elif m.isnumeric() == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Mobile number should be numeric")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        elif m!="" and len(m) != 10:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Moblie number should be 10 digit")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

        elif e=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Email field cann't be empty")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

        elif e!="" and emailValid == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter valid email address")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

        elif p == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter Password")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        
        elif rp == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Re-enter Password")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

        else:
            if p == rp:
                q = "insert into librarianRegistration values (?,?,?,?)"
                cur.execute(q,(n,m,e,p))
                con.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("One row inserted")
                msg.setWindowTitle("Ok")
                msg.show()
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Password not matched")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    librarian_registration = QtWidgets.QMainWindow()
    ui = Ui_librarian_registration()
    ui.setupUi(librarian_registration)
    librarian_registration.show()
    sys.exit(app.exec_())
