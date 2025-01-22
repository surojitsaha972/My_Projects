from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_CSP(object):
    def setupUi(self, CSP):
        CSP.setObjectName("CSP")
        CSP.resize(1368, 878)
        CSP.setMinimumSize(QtCore.QSize(1368, 878))
        CSP.setMaximumSize(QtCore.QSize(1368, 878))
        self.centralwidget = QtWidgets.QWidget(CSP)
        self.centralwidget.setObjectName("centralwidget")
        self.F1 = QtWidgets.QFrame(self.centralwidget)
        self.F1.setGeometry(QtCore.QRect(-60, 0, 1401, 831))
        self.F1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.F1.setStyleSheet("background-color: rgb(192, 200, 209);\n"
"border-radius:20px;")
        self.F1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F1.setObjectName("F1")
        self.F2 = QtWidgets.QFrame(self.F1)
        self.F2.setGeometry(QtCore.QRect(0, 0, 241, 821))
        self.F2.setStyleSheet("background-color: lightblue;\n"
"border-radius:20px;")
        self.F2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.F2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.F2.setObjectName("F2")
        self.ACCT = QtWidgets.QRadioButton(self.F1)
        self.ACCT.setGeometry(QtCore.QRect(640, 80, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ACCT.setFont(font)
        self.ACCT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ACCT.setObjectName("ACCT")
        self.NAME = QtWidgets.QRadioButton(self.F1)
        self.NAME.setGeometry(QtCore.QRect(790, 80, 95, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NAME.setFont(font)
        self.NAME.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NAME.setObjectName("NAME")
        self.LOAN = QtWidgets.QRadioButton(self.F1)
        self.LOAN.setGeometry(QtCore.QRect(910, 80, 95, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LOAN.setFont(font)
        self.LOAN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LOAN.setObjectName("LOAN")
        self.b1 = QtWidgets.QPushButton(self.F1)
        self.b1.setGeometry(QtCore.QRect(670, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.setStyleSheet("background-color: grey;\n"
"border:10px;")
        self.b1.setObjectName("b1")
        self.label = QtWidgets.QLabel(self.F1)
        self.label.setGeometry(QtCore.QRect(510, 260, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.F1)
        self.label_2.setGeometry(QtCore.QRect(510, 310, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.F1)
        self.label_3.setGeometry(QtCore.QRect(510, 360, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.F1)
        self.label_4.setGeometry(QtCore.QRect(510, 420, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.F1)
        self.label_5.setGeometry(QtCore.QRect(510, 530, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.F1)
        self.label_7.setGeometry(QtCore.QRect(510, 470, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.sear = QtWidgets.QLineEdit(self.F1)
        self.sear.setGeometry(QtCore.QRect(640, 120, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sear.setFont(font)
        self.sear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sear.setAutoFillBackground(False)
        self.sear.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sear.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.sear.setAlignment(QtCore.Qt.AlignCenter)
        self.sear.setObjectName("sear")
        self.nam = QtWidgets.QLabel(self.F1)
        self.nam.setGeometry(QtCore.QRect(620, 260, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nam.setFont(font)
        self.nam.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.nam.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.nam.setText("")
        self.nam.setObjectName("nam")
        self.ph = QtWidgets.QLabel(self.F1)
        self.ph.setGeometry(QtCore.QRect(620, 310, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ph.setFont(font)
        self.ph.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.ph.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ph.setText("")
        self.ph.setObjectName("ph")
        self.em = QtWidgets.QLabel(self.F1)
        self.em.setGeometry(QtCore.QRect(620, 360, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em.setFont(font)
        self.em.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.em.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.em.setText("")
        self.em.setObjectName("em")
        self.add = QtWidgets.QLabel(self.F1)
        self.add.setGeometry(QtCore.QRect(620, 420, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.add.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.add.setText("")
        self.add.setObjectName("add")
        self.bn = QtWidgets.QLabel(self.F1)
        self.bn.setGeometry(QtCore.QRect(620, 480, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bn.setFont(font)
        self.bn.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.bn.setStyleSheet("\n"
"background-color:rgb(255, 255, 255)")
        self.bn.setText("")
        self.bn.setObjectName("bn")
        self.acct = QtWidgets.QLabel(self.F1)
        self.acct.setGeometry(QtCore.QRect(620, 530, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acct.setFont(font)
        self.acct.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.acct.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.acct.setText("")
        self.acct.setObjectName("acct")
        self.label_15 = QtWidgets.QLabel(self.F1)
        self.label_15.setGeometry(QtCore.QRect(510, 570, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.dueD = QtWidgets.QLabel(self.F1)
        self.dueD.setGeometry(QtCore.QRect(620, 580, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dueD.setFont(font)
        self.dueD.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.dueD.setStyleSheet("\n"
"background-color: rgb(255, 255, 255)")
        self.dueD.setText("")
        self.dueD.setObjectName("dueD")
        self.label_17 = QtWidgets.QLabel(self.F1)
        self.label_17.setGeometry(QtCore.QRect(700, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_8 = QtWidgets.QLabel(self.F1)
        self.label_8.setGeometry(QtCore.QRect(520, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        CSP.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CSP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 27))
        self.menubar.setObjectName("menubar")
        CSP.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CSP)
        self.statusbar.setObjectName("statusbar")
        CSP.setStatusBar(self.statusbar)

        self.b1.clicked.connect(self.search)

        self.retranslateUi(CSP)
        QtCore.QMetaObject.connectSlotsByName(CSP)

    def retranslateUi(self, CSP):
        _translate = QtCore.QCoreApplication.translate
        CSP.setWindowTitle(_translate("CSP", "Searchingpage"))
        self.ACCT.setText(_translate("CSP", "ACCTOUNT NO"))
        self.NAME.setText(_translate("CSP", "NAME"))
        self.LOAN.setText(_translate("CSP", "LOAN ID"))
        self.b1.setText(_translate("CSP", "SEARCH"))
        self.label.setText(_translate("CSP", "NAME"))
        self.label_2.setText(_translate("CSP", "PHONE NO"))
        self.label_3.setText(_translate("CSP", "EMAIL"))
        self.label_4.setText(_translate("CSP", "ADDRESS"))
        self.label_5.setText(_translate("CSP", "ACCT NO:"))
        self.label_7.setText(_translate("CSP", "BANK NAME"))
        self.sear.setPlaceholderText(_translate("CSP", "Enter search value "))
        self.label_15.setText(_translate("CSP", "DUE DATE"))
        self.label_17.setText(_translate("CSP", "SEARCHING PAGE"))
        self.label_8.setText(_translate("CSP", "SEARCH TYPE"))


    def search(self):
        sVal = self.sear.text()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()

        if self.ACCT.isChecked():    
        #     Stype = "Account"
            q = "select name, mail, phone, address, bankName, Account from approveRequest where Account = ?"
            cur.execute(q,(sVal,))
            res = cur.fetchall()

            if res == []:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("NO data found")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()

            else:
                # print(res)
                newList = []
                for i in res:
                        for element in i:
                                newList.append(element)
                # name = newList[0]
                # email = newList[1]
                # phone = newList[2]
                # address = newList[3]
                # bankN = newList[4]
                # acNo = newList[5]

                self.nam.setText(newList[0])
                self.ph.setText(newList[2])
                self.em.setText(newList[1])
                self.add.setText(newList[3])
                self.bn.setText(newList[4])
                self.acct.setText(newList[5])

             

        if self.NAME.isChecked():
        #     Stype = "name"
        #     self.label_8.setText("Name")
            q = "select name, mail, phone, address, bankName, Account from approveRequest where phone = ?"
            cur.execute(q,(sVal,))
            res = cur.fetchall()
        #     print(res)
            if res == []:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("NO data found")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()

            else:
                # print(res)
                newList = []
                for i in res:
                        for element in i:
                                newList.append(element)
                # name = newList[0]
                # email = newList[1]
                # phone = newList[2]
                # address = newList[3]
                # bankN = newList[4]
                # acNo = newList[5]

                self.nam.setText(newList[0])
                self.ph.setText(newList[2])
                self.em.setText(newList[1])
                self.add.setText(newList[3])
                self.bn.setText(newList[4])
                self.acct.setText(newList[5])
        
        if self.LOAN.isChecked():
        #     Stype = "lid"
        #     self.label_8.setText("Loan")
            q = "select name, mail, phone, address, bankName, Account from approveRequest where lid = ?"
            cur.execute(q,(sVal,))
            res = cur.fetchall()
        #     print(res)
            if res == []:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("NO data found")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()

            else:
                # print(res)
                newList = []
                for i in res:
                        for element in i:
                                newList.append(element)
                # name = newList[0]
                # email = newList[1]
                # phone = newList[2]
                # address = newList[3]
                # bankN = newList[4]
                # acNo = newList[5]

                self.nam.setText(newList[0])
                self.ph.setText(newList[2])
                self.em.setText(newList[1])
                self.add.setText(newList[3])
                self.bn.setText(newList[4])
                self.acct.setText(newList[5])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CSP = QtWidgets.QMainWindow()
    ui = Ui_CSP()
    ui.setupUi(CSP)
    CSP.show()
    sys.exit(app.exec_())
