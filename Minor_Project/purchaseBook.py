# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchaseBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from datetime import date
import time

class Ui_purchaseBook(object):
    def setupUi(self, purchaseBook):
        purchaseBook.setObjectName("purchaseBook")
        purchaseBook.resize(800, 597)
        self.centralwidget = QtWidgets.QWidget(purchaseBook)
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
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.subName = QtWidgets.QComboBox(self.frame_2)
        self.subName.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("MoolBoran")
        font.setPointSize(16)
        self.subName.setFont(font)
        self.subName.setObjectName("subName")
        self.subName.addItem("")
        self.subName.setItemText(0, "")
        self.horizontalLayout.addWidget(self.subName)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(450, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table = QtWidgets.QTableWidget(self.frame_3)
        self.table.setMinimumSize(QtCore.QSize(20, 0))
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.table)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.price = QtWidgets.QLineEdit(self.frame_4)
        self.price.setObjectName("price")
        self.horizontalLayout_2.addWidget(self.price)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.qnt = QtWidgets.QLineEdit(self.frame_5)
        self.qnt.setObjectName("qnt")
        self.horizontalLayout_3.addWidget(self.qnt)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.calPrice = QtWidgets.QPushButton(self.frame_6)
        self.calPrice.setObjectName("calPrice")
        self.horizontalLayout_4.addWidget(self.calPrice)
        self.verticalLayout.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.finalPrice = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.finalPrice.setFont(font)
        self.finalPrice.setObjectName("finalPrice")
        self.horizontalLayout_5.addWidget(self.finalPrice)
        self.verticalLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.purchase = QtWidgets.QPushButton(self.frame_8)
        self.purchase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.purchase.setObjectName("purchase")
        self.horizontalLayout_6.addWidget(self.purchase)
        self.verticalLayout.addWidget(self.frame_8, 0, QtCore.Qt.AlignHCenter)
        purchaseBook.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(purchaseBook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        purchaseBook.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(purchaseBook)
        self.statusbar.setObjectName("statusbar")
        purchaseBook.setStatusBar(self.statusbar)

        self.retranslateUi(purchaseBook)
        QtCore.QMetaObject.connectSlotsByName(purchaseBook)

        self.calPrice.clicked.connect(self.pri)
        self.purchase.clicked.connect(self.pur)
        self.subName.currentIndexChanged.connect(self.comboIndex)
        self.showBooks()

    def retranslateUi(self, purchaseBook):
        _translate = QtCore.QCoreApplication.translate
        purchaseBook.setWindowTitle(_translate("purchaseBook", "Purchase Book"))
        self.label.setText(_translate("purchaseBook", "Purchase book"))
        self.label_7.setText(_translate("purchaseBook", "Subject Name"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("purchaseBook", "AuthorName"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("purchaseBook", "BookName"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("purchaseBook", "Edition"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("purchaseBook", "Stock"))
        self.label_2.setText(_translate("purchaseBook", "Price"))
        self.label_4.setText(_translate("purchaseBook", "Quantity"))
        self.calPrice.setText(_translate("purchaseBook", "Calculate Price"))
        self.label_3.setText(_translate("purchaseBook", "Final Price"))
        self.finalPrice.setText(_translate("purchaseBook", ""))
        self.purchase.setText(_translate("purchaseBook", "Purchase"))

    def showBooks(self):
        bn = self.subName.currentText()
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q = "select SubjectName from addSubject "
        cur.execute(q,(bn))
        c = cur.fetchall()
        # l =[]
        for i in c :
            # if i not in l:
                # l.append(i)
            self.subName.addItem(i[0])
        

    def comboIndex(self):
        sn = self.subName.currentText()
        # print(bn)
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q = "select AuthorName, BookName ,Edition, Stock from bookStock where SubjectName = ?"
        cur.execute(q,(sn,))
        res = cur.fetchall()
        # print(res)
        self.table.setRowCount(0)
        for i in res:
            rc = self.table.rowCount()
            self.table.insertRow(rc)
            self.table.setItem(rc,0,QtWidgets.QTableWidgetItem(i[0]))
            self.table.setItem(rc,1,QtWidgets.QTableWidgetItem(i[1]))
            self.table.setItem(rc,2,QtWidgets.QTableWidgetItem(str(i[2])))
            self.table.setItem(rc,3,QtWidgets.QTableWidgetItem(str(i[3])))
        # self.qnt.setText("1")

    def pri(self):
        try:
            qnt = self.qnt.text().lstrip().rstrip()
            amt = self.price.text().lstrip().rstrip()
            i = self.table.currentIndex()
            rw = i.row()
            # print(rw)
            # pub = int(self.table.item(rw,2).text())
            if rw == -1:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Select any book")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
            else:
                fp = int(amt) * int(qnt)
                self.finalPrice.setText(str(fp))
        
        except ValueError:
            if qnt == '' or amt == '':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Fields cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Quantity must be of integer type")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()

    def pur(self):
        p = self.finalPrice.text()
        qnt = int(self.qnt.text())
        sn = self.subName.currentText()
        ind = self.table.currentIndex()
        rw = ind.row()
        aut = self.table.item(rw,0).text()
        bn = self.table.item(rw,1).text()
        ed = self.table.item(rw,2).text()
        
        dt = date.today()
        ti = time.strftime("%H:%M:%S",time.localtime())
        
        con = sqlite3.connect("projectDB.db")
        
        cur = con.cursor()

        # print(qnt,sn,bn,ed,aut)
        q1 = "update bookStock set Stock = (Stock + ?) where SubjectName = ? and BookName = ? and Edition = ? and AuthorName = ?"
        cur.execute(q1,(qnt,sn,bn,ed,aut))
        
        cur1 = con.cursor()
        q2 = "insert into purchaseBook values (?,?,?,?,?,?,?,?)"
        cur1.execute(q2,(sn,bn,aut,ed,qnt,p,dt,ti))
        con.commit()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Purchase succesfully")
        msg.setWindowTitle("Purchase")
        msg.show()
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseBook = QtWidgets.QMainWindow()
    ui = Ui_purchaseBook()
    ui.setupUi(purchaseBook)
    purchaseBook.show()
    sys.exit(app.exec_())
