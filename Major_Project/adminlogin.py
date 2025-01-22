from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from emailpass import mailid, password
from email.message import EmailMessage
import ssl
import smtplib
from adminregistration import*
from dashboard import *

class Ui_ADMINLOGIN(object):
    def setupUi(self, ADMINLOGIN):
        ADMINLOGIN.setObjectName("ADMINLOGIN")
        ADMINLOGIN.resize(1368, 927)
        ADMINLOGIN.setMinimumSize(QtCore.QSize(1368, 878))
        ADMINLOGIN.setMaximumSize(QtCore.QSize(1368, 1368))
        self.centralwidget = QtWidgets.QWidget(ADMINLOGIN)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 0, 1368, 878))
        self.frame.setMinimumSize(QtCore.QSize(1368, 878))
        self.frame.setMaximumSize(QtCore.QSize(1368, 878))
        self.frame.setStyleSheet("background:rgb(252, 255, 234)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(330, 10, 661, 831))
        self.widget.setStyleSheet("background:rgb(255, 244, 235)")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 410, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:rgb(242, 255, 244)")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 480, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background:rgb(242, 255, 244)")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 560, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background:rgb(228, 231, 255)")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 261, 231))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(100)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 219, 193)\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.forget = QtWidgets.QPushButton(self.widget)
        self.forget.setGeometry(QtCore.QRect(370, 610, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.forget.setFont(font)
        self.forget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forget.setStyleSheet("background:rgb(228, 231, 255)")
        self.forget.setObjectName("forget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(120, 410, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(120, 480, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 30, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:rgb(246, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.signup = QtWidgets.QPushButton(self.widget)
        self.signup.setGeometry(QtCore.QRect(150, 610, 131, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setStyleSheet("background:rgb(228, 231, 255)")
        self.signup.setObjectName("signup")

        self.signup.clicked.connect(self.dis)

        ADMINLOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ADMINLOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 26))
        self.menubar.setObjectName("menubar")
        ADMINLOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ADMINLOGIN)
        self.statusbar.setObjectName("statusbar")
        ADMINLOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(ADMINLOGIN)
        QtCore.QMetaObject.connectSlotsByName(ADMINLOGIN)

        self.pushButton.clicked.connect(self.login)
        self.forget.clicked.connect(self.forgetPass)


    def retranslateUi(self, ADMINLOGIN):
        _translate = QtCore.QCoreApplication.translate
        ADMINLOGIN.setWindowTitle(_translate("ADMINLOGIN", "Admin Login"))
        self.lineEdit.setPlaceholderText(_translate("ADMINLOGIN", "  Email_id"))
        self.lineEdit_2.setPlaceholderText(_translate("ADMINLOGIN", "  Password"))
        self.pushButton.setText(_translate("ADMINLOGIN", "Log In "))
        self.label_2.setText(_translate("ADMINLOGIN", ""))
        self.forget.setText(_translate("ADMINLOGIN", "Forgot Password?"))
        self.label.setText(_translate("ADMINLOGIN", "Email:"))
        self.label_3.setText(_translate("ADMINLOGIN", "PASSWORD:"))
        self.label_4.setText(_translate("ADMINLOGIN", "ADMIN LOGIN"))
        self.signup.setText(_translate("ADMINLOGIN", "Sign Up"))

    def login(self):
        e = self.lineEdit.text()
        p = self.lineEdit_2.text()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        query = "select count(email), Email, Password from AdminLogin where Password = ? and Email = ?"
        cur.execute(query,(p,e))
        res = cur.fetchall()
        l=[]
        
        query = "select Password,Email from AdminLogin where Email = ?"
        cur.execute(query,(e,))
        pas = cur.fetchall()
        if p=="" and e == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Field cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
                

        elif p=="": 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Password field cann't be empty")
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

        elif pas == l:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Wrong Email")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
            
        elif pas[0][1] == e and pas[0][0] != p:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Wrong Password")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
        else:
                # msg = QMessageBox()
                # msg.setIcon(QMessageBox.Information)
                # msg.setText("Successfully login")
                # msg.setWindowTitle("Login succesful")
                # msg.show()
                # msg.exec_()

                self.dashBoard = QtWidgets.QMainWindow()
                self.ui = Ui_dashBoard(e)
                self.ui.setupUi(self.dashBoard)
                self.dashBoard.show()
        con.commit()
    
    def forgetPass(self): 
        e = self.lineEdit.text()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        
        query = "select Password from AdminLogin where Email = ?"
        cur.execute(query,(e,))
        res = cur.fetchall()
        l = []

        if e =="":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Enter Email on the field")
                msg.setWindowTitle("Enter mail")
                msg.show()
                msg.exec_()
        elif res == l:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Wrong Email")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
        else:
                body = "Your password is " + res[0][0]

                em = EmailMessage()
                em['From'] = mailid
                em['To'] = e
                em['subject'] = body
                em.set_content(body)      
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
                        smtp.login(mailid,password)
                        smtp.sendmail(mailid, e, em.as_string())

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Password sent to your registered email id")
                msg.setWindowTitle("Password")
                msg.show()
                msg.exec_()
            
        
    def dis(self):
        self.Adminreg = QtWidgets.QMainWindow()
        self.ui = Ui_Adminreg()
        self.ui.setupUi(self.Adminreg)
        self.Adminreg.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ADMINLOGIN = QtWidgets.QMainWindow()
    ui = Ui_ADMINLOGIN()
    ui.setupUi(ADMINLOGIN)
    ADMINLOGIN.show()
    sys.exit(app.exec_())
