# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'returnBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date
from PyQt5.QtWidgets import QMessageBox
from finePage import *
from email.message import EmailMessage
import ssl
import smtplib
from emailPass import mailid,password

class Ui_returnBook(object):
    def setupUi(self, returnBook):
        returnBook.setObjectName("returnBook")
        returnBook.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(returnBook)
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
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sid = QtWidgets.QLineEdit(self.frame_2)
        self.sid.setObjectName("sid")
        self.horizontalLayout.addWidget(self.sid)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.search = QtWidgets.QPushButton(self.frame_3)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search.setObjectName("search")
        self.verticalLayout_3.addWidget(self.search)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table = QtWidgets.QTableWidget(self.frame_4)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.table)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.returnB = QtWidgets.QPushButton(self.frame_5)
        self.returnB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.returnB.setObjectName("returnB")
        self.verticalLayout_4.addWidget(self.returnB)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        returnBook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(returnBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        returnBook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(returnBook)
        self.statusbar.setObjectName("statusbar")
        returnBook.setStatusBar(self.statusbar)

        self.retranslateUi(returnBook)
        QtCore.QMetaObject.connectSlotsByName(returnBook)

        
        self.table.setVisible(False)
        self.returnB.setVisible(False)
        self.search.clicked.connect(self.find)
        self.returnB.clicked.connect(self.retBook)
        self.returnB.clicked.connect(returnBook.close)

    def retranslateUi(self, returnBook):
        _translate = QtCore.QCoreApplication.translate
        returnBook.setWindowTitle(_translate("returnBook", "Return Book"))
        self.label.setText(_translate("returnBook", "Return Book"))
        self.label_3.setText(_translate("returnBook", "Enter SID"))
        self.search.setText(_translate("returnBook", "Search"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("returnBook", "AccessionNo"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("returnBook", "IssueDate"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("returnBook", "DueDate"))
        self.returnB.setText(_translate("returnBook", "Return"))

    def find(self):
        sid = self.sid.text().lstrip().rstrip()
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q = "select BookID, SID, IssueDate, DueDate from issueBook where SID = ? and ReturnDate = ?"
        cur.execute(q,(sid,"NULL"))
        res = cur.fetchall()
        l = []
        self.table.setRowCount(0)

        if res != l:
            self.table.setVisible(True)
            self.returnB.setVisible(True)

            for i in res:
                rc = self.table.rowCount()
                self.table.insertRow(rc)
                self.table.setItem(rc,0,QtWidgets.QTableWidgetItem(i[0]))
                self.table.setItem(rc,1,QtWidgets.QTableWidgetItem(i[2]))
                self.table.setItem(rc,2,QtWidgets.QTableWidgetItem(i[3]))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Incorect SID")
            msg.setWindowTitle("Incorect")
            msg.show()
            msg.exec_()

    def retBook(self):
        ind = self.table.currentIndex()
        rw = ind.row()
        if rw == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Select any book")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

        else:  
            
            bid = self.table.item(rw,0).text()
            sid = int(self.sid.text())
            
            due = self.table.item(rw,2).text()
            y,m,d = map(int,due.split('-'))
            duedate = date(y,m,d)
            today = date.today()
            
            con = sqlite3.connect("projectDB.db")
            cur = con.cursor()
            q = "select SubjectName, BookName, AuthorName, Edition from issueBook where BookID = ? and SID = ? and ReturnDate = ?"
            cur.execute(q,(bid,sid,"NULL"))
            res = cur.fetchall()

            sn = res[0][0]
            bn = res[0][1]
            ed = res[0][3]
            an = res[0][2]
            
            if today <= duedate:
                cur = con.cursor()
                q1 = "update bookStock set Stock = (Stock + 1) where SubjectName = ? and BookName = ? and Edition = ? and AuthorName = ?"
                cur.execute(q1,(sn,bn,ed,an))
                cur = con.cursor()
                q = "update issueBook set ReturnDate = ? where BookID = ? and SID = ? and ReturnDate = ?"
                cur.execute(q,(today,bid,sid,"NULL"))
                
                con.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Book returned")
                msg.setWindowTitle("Return Book")
                msg.show()
                msg.exec_()
                self.table.removeRow(rw)
                self.sid.setText(" ")

                cur = con.cursor()
                q = "select Email, Name from studentReg where SID = ?"
                cur.execute(q,(sid,))
                res = cur.fetchall()
                # print(res[0][0])

                receiver = res[0][0]
                name = res[0][1]
                sub = "Book returned"
                body = f"Dear {name},\n\nYour book which name: {bn}, edition: {ed}, author name: {an}, book id: {bid} has returned."
                
                em = EmailMessage()
                em['From'] = mailid
                em['To'] = receiver
                em['subject'] = sub
                em.set_content(body)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
                    smtp.login(mailid,password)
                    smtp.sendmail(mailid, receiver, em.as_string())

            else:
                fine = int((today - duedate).days)*10
                m = "Due date is over! FINE AMOUNT " 
                m = m + str(fine)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(m)
                msg.setWindowTitle("Return Book")
                msg.show()
                msg.exec_()

                self.finePage = QtWidgets.QMainWindow()
                self.ui = Ui_finePage(sid,bid,fine,sn,bn,ed,an,duedate)
                self.ui.setupUi(self.finePage)
                self.finePage.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    returnBook = QtWidgets.QMainWindow()
    ui = Ui_returnBook()
    ui.setupUi(returnBook)
    returnBook.show()
    sys.exit(app.exec_())
