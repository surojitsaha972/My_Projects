from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from datetime import timedelta,date
from emailPass import mailid,password
from email.message import EmailMessage
import ssl
import smtplib
from changePassword import *
from dashboard import *
from dashboard2 import *

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(853, 598)
        self.centralwidget = QtWidgets.QWidget(login)
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
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(88, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setMinimumSize(QtCore.QSize(278, 0))
        self.email.setMaximumSize(QtCore.QSize(16777215, 30))
        self.email.setObjectName("email")
        self.horizontalLayout_2.addWidget(self.email)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(91, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.frame_3)
        self.password.setMinimumSize(QtCore.QSize(278, 0))
        self.password.setMaximumSize(QtCore.QSize(16777215, 30))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loginButton = QtWidgets.QPushButton(self.frame_4)
        self.loginButton.setMinimumSize(QtCore.QSize(92, 0))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout.addWidget(self.frame_5)
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 21))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

        self.loginButton.clicked.connect(self.logButton)
        # self.loginButton.clicked.connect(login.close)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.label.setText(_translate("login", "Library Management System"))
        self.label_2.setText(_translate("login", "Email"))
        self.label_3.setText(_translate("login", "Password"))
        self.loginButton.setText(_translate("login", "Login"))

    def logButton(self):
        e = self.email.text()
        p = self.password.text()
        # print(e)
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        
        query = "select count(email), Email, Password from admin where Password = ? and Email = ?"
        cur.execute(query,(p,e))
        res = cur.fetchall()
        
        query = "select Password,Email,Name,MobileNo from admin where Email = ?"
        cur.execute(query,(e,))
        pas = cur.fetchall()
        # print(pas)
        # print(name)
        # print(pas)
        l = []
        dt = date.today()

        if res[0][0] == 1:
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # msg.setText("Login Succesful")
            # msg.setWindowTitle("OK")
            # msg.show()
            # msg.exec_()

            name = pas[0][2]
            mobile = pas[0][3]
            # self.dashBoard = QtWidgets.QMainWindow()
            # self.ui = Ui_dashBoard(e,name,mobile)
            # # self.ui = Ui_dashBoard(e)
            # self.ui.setupUi(self.dashBoard)
            # self.dashBoard.show()

            self.dashBoard = QtWidgets.QMainWindow()
            self.ui = Ui_dashBoard(e,name,mobile)
            self.ui.setupUi(self.dashBoard)
            self.dashBoard.show()

            # DELETE PENDING BOOK REQUESTS

            cur = con.cursor()
            q = "select SID, SubjectName, BookName, AuthorName, Edition from bookRequest where Date < ?"
            # q1 = "del bookRequest where date < ?"
            cur.execute(q,(dt,))
            res = cur.fetchall()
            # sid = res[0][0]
            # print(res[0][0])
            # cur = con.cursor()
            # q = ""
            if res != l:
                for i in res:
                    cur1 = con.cursor()
                    q1 = "update bookStock set Stock = (Stock + 1) where SubjectName = ? and BookName = ? and Edition = ? and AuthorName = ?"
                    cur1.execute(q1,(i[1],i[2],i[4],i[3]))

                q2 = "delete from bookRequest where Date < ?"
                cur2 = con.cursor()
                cur2.execute(q2,(dt,))

            # BOOK RETURN REMAINDER

            a3 = dt + timedelta(days=3)
            con = sqlite3.connect("projectDB.db")
            cur = con.cursor()
            q = "select SID, BookID, BookName, AuthorName, Edition from issueBook where DueDate = ? and ReturnDate = ? and DueReminder = ?"
            cur.execute(q,(a3,'NULL',0))
            res1 = cur.fetchall()

            
            if res1 != l:
                cur1 = con.cursor()
                sub = "Return remainder"
                for i in res1:
                    q = "select Email, Name from studentReg where SID = ?"
                    cur1.execute(q,(i[0],))
                    res2 = cur1.fetchall()
                    
                    receiver = res2[0][0]
                    name = res2[0][1]

                    body = f"Dear {name},\n\nYour book which name: {i[2]}, edition: {i[4]}, author name: {i[3]}, book id: {i[1]} will due in next 3 days.\nSo return the book within 3 days to avoid overdue of book."
                    # print(receiver,name)
                    # print(body)
                    em = EmailMessage()
                    em['From'] = mailid
                    em['To'] = receiver
                    em['subject'] = sub
                    em.set_content(body)

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
                        smtp.login(mailid,password)
                        smtp.sendmail(mailid, receiver, em.as_string())
                    
                    cur4 = con.cursor()
                    q = "update issueBook set DueReminder = ? where BookID = ? and SID = ? and ReturnDate = ? "
                    cur4.execute(q,(1,i[1],i[0],"NULL"))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Mail Sent")
                msg.setWindowTitle("OK")
                msg.show()
                msg.exec_()
            
            # else:
            #     print("No mail")
            # print(a3,res)
            # print("hello")

            self.email.setText('')
            self.password.setText('')
            
        else:
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
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Wrong Password")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
                
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Successfully login")
                msg.setWindowTitle("Login Unsuccesful")
                msg.show()
                msg.exec_()
        con.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
