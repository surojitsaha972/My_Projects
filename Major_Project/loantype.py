from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_LoanType(object):
    def setupUi(self, LoanType):
        LoanType.setObjectName("LoanType")
        LoanType.resize(1368, 878)
        LoanType.setMinimumSize(QtCore.QSize(1368, 878))
        LoanType.setMaximumSize(QtCore.QSize(1368, 878))
        self.centralwidget = QtWidgets.QWidget(LoanType)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 40, 971, 741))
        self.frame.setStyleSheet("background-color: rgb(94, 200, 200);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.l1 = QtWidgets.QLabel(self.frame)
        self.l1.setGeometry(QtCore.QRect(290, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("background-color: rgb(255, 192, 203);")
        self.l1.setObjectName("l1")
        self.subbut = QtWidgets.QPushButton(self.frame)
        self.subbut.setGeometry(QtCore.QRect(380, 430, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subbut.setFont(font)
        self.subbut.setStyleSheet("background:rgb(182, 182, 182)")
        self.subbut.setObjectName("subbut")
        self.loantext = QtWidgets.QLineEdit(self.frame)
        self.loantext.setGeometry(QtCore.QRect(460, 321, 221, 41))
        self.loantext.setStyleSheet("background-color: rgb(236, 236, 136);\n"
"background-color: rgb(243, 243, 241);")
        self.loantext.setObjectName("loantext")
        LoanType.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoanType)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 27))
        self.menubar.setObjectName("menubar")
        LoanType.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoanType)
        self.statusbar.setObjectName("statusbar")
        LoanType.setStatusBar(self.statusbar)

        self.subbut.clicked.connect(self.addloantype)

        self.retranslateUi(LoanType)
        QtCore.QMetaObject.connectSlotsByName(LoanType)

    def retranslateUi(self, LoanType):
        _translate = QtCore.QCoreApplication.translate
        LoanType.setWindowTitle(_translate("LoanType", "Loan_Type"))
        self.l1.setText(_translate("LoanType", "  LOAN TYPE:"))
        self.subbut.setText(_translate("LoanType", "SUBMIT"))

    def addloantype(self):
        t=self.loantext.text().lstrip().rstrip()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        if t=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Loan type field cann't be empty")
            msg.setWindowTitle("Loan Type")
            msg.show()
            msg.exec_()
        else:
            q = "insert into Loan_Type values (?)"
            cur.execute(q,(t,))
            con.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("1 loan type is added")
            msg.setWindowTitle("Loan Type")
            msg.show()
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoanType = QtWidgets.QMainWindow()
    ui = Ui_LoanType()
    ui.setupUi(LoanType)
    LoanType.show()
    sys.exit(app.exec_())
