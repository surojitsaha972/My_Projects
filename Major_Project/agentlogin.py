from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from emailpass import mailid, password
from email.message import EmailMessage
import ssl
import smtplib

class Ui_Login_Page(object):
    def setupUi(self, Login_Page):
        Login_Page.setObjectName("Login_Page")
        Login_Page.resize(1368, 878)
        Login_Page.setMinimumSize(QtCore.QSize(1368, 878))
        Login_Page.setMaximumSize(QtCore.QSize(1368, 878))
        Login_Page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(Login_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(450, 30, 431, 741))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-200, 20, 981, 691))
        self.label.setStyleSheet("background-color:rgba(16,30,41,240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 410, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 480, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(60, 560, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"paddimg-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 261, 231))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(100)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0,125,236,255);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.forget = QtWidgets.QPushButton(self.widget)
        self.forget.setGeometry(QtCore.QRect(240, 610, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.forget.setFont(font)
        self.forget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forget.setStyleSheet("background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;")
        self.forget.setObjectName("forget")
        Login_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 27))
        self.menubar.setObjectName("menubar")
        Login_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_Page)
        self.statusbar.setObjectName("statusbar")
        Login_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Login_Page)
        QtCore.QMetaObject.connectSlotsByName(Login_Page)

        self.pushButton.clicked.connect(self.login)
        self.forget.clicked.connect(self.forgetPass)

    def retranslateUi(self, Login_Page):
        _translate = QtCore.QCoreApplication.translate
        Login_Page.setWindowTitle(_translate("Login_Page", "Agent_Login"))
        self.lineEdit.setPlaceholderText(_translate("Login_Page", "  Email_id"))
        self.lineEdit_2.setPlaceholderText(_translate("Login_Page", "  Password"))
        self.pushButton.setText(_translate("Login_Page", "Log In "))
        self.label_2.setText(_translate("Login_Page", ""))
        self.forget.setText(_translate("Login_Page", "Forgot Password?"))

    def login(self):
        e = self.lineEdit.text()
        p = self.lineEdit_2.text()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        query = "select count(email), Email, Password from login where Password = ? and Email = ?"
        cur.execute(query,(p,e))
        res = cur.fetchall()
        l=[]
        
        query = "select Password,Email from login where Email = ?"
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
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Successfully login")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
        con.commit()
    
    def forgetPass(self): 
        e = self.lineEdit.text()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        
        query = "select Password from login where Email = ?"
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Page = QtWidgets.QMainWindow()
    ui = Ui_Login_Page()
    ui.setupUi(Login_Page)
    Login_Page.show()
    sys.exit(app.exec_())
