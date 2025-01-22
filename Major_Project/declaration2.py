from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dec(object):
    def setupUi(self, dec):
        dec.setObjectName("dec")
        dec.resize(1387, 878)
        dec.setMinimumSize(QtCore.QSize(1387, 878))
        dec.setMaximumSize(QtCore.QSize(1387, 878))
        self.centralwidget = QtWidgets.QWidget(dec)
        self.centralwidget.setObjectName("centralwidget")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(610, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setStyleSheet("background:rgb(211, 207, 255)")
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(40, 140, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(410, 135, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(600, 130, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setObjectName("t2")
        self.l5 = QtWidgets.QLabel(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(1130, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(60, 131, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setObjectName("t1")
        self.t1_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1_2.setGeometry(QtCore.QRect(40, 180, 881, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.t1_2.setFont(font)
        self.t1_2.setObjectName("t1_2")
        self.l2_2 = QtWidgets.QLabel(self.centralwidget)
        self.l2_2.setGeometry(QtCore.QRect(930, 180, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l2_2.setFont(font)
        self.l2_2.setObjectName("l2_2")
        self.l2_3 = QtWidgets.QLabel(self.centralwidget)
        self.l2_3.setGeometry(QtCore.QRect(40, 500, 1251, 181))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.l2_3.setFont(font)
        self.l2_3.setStyleSheet("background:rgb(255, 78, 81)")
        self.l2_3.setObjectName("l2_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 730, 1241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.l2_4 = QtWidgets.QLabel(self.centralwidget)
        self.l2_4.setGeometry(QtCore.QRect(40, 230, 1381, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l2_4.setFont(font)
        self.l2_4.setStyleSheet("background:rgb(242, 255, 230)")
        self.l2_4.setObjectName("l2_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 780, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        dec.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dec)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1387, 26))
        self.menubar.setObjectName("menubar")
        dec.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dec)
        self.statusbar.setObjectName("statusbar")
        dec.setStatusBar(self.statusbar)

        self.checkBox.stateChanged.connect(self.check)
        self.pushButton.setVisible(False)
        self.pushButton.clicked.connect(dec.close)

        self.retranslateUi(dec)
        QtCore.QMetaObject.connectSlotsByName(dec)

    def retranslateUi(self, dec):
        _translate = QtCore.QCoreApplication.translate
        dec.setWindowTitle(_translate("dec", "Declaration Page"))
        self.l1.setText(_translate("dec", "DECLARATION FORM"))
        self.l2.setText(_translate("dec", "I"))
        self.l3.setText(_translate("dec", "son/daughter of"))
        self.l5.setText(_translate("dec", " resident of"))
        self.l2_2.setText(_translate("dec", "I willing to take loan under this conditions."))
        self.l2_3.setText(_translate("dec", "I do solemnly and sincerely declare and state in signing this document that I:\n"
"\n"
"\n"
"   *Acknowledge that I have read, understood, and accepted the terms and conditions of the Urgent Money Receive loans electronically;\n"
"   * Agree to the electronic storage of my personal information and the Terms and Conditions of the Urgent Money Receive loans \n"
"       which I accepted;\n"
"   * Acknowledge that my application does not guarantee me acceptance for a specific loan type;\n"
"   Agree to pay the insurance premium associated with my loan in the events it is approved and I meet the requirements for same;"))
        self.checkBox.setText(_translate("dec", "  I hereby declare that whatever has been stated above is true to the best of my knowledge, correct and nothing marerial has been concealed\n"
"  there form."))
        self.l2_4.setText(_translate("dec", "1.Job ID: This is typically a unique identifier assigned to your job or employment status.\n"
" It\'s often used by lenders to verify your employment details and stability.\n"
"2.Credit score: 720+ This indicates a good credit score.\n"
" Credit scores range from 300 to 850 in India, with higher scores indicating lower credit risk.\n"
" A score of 720 or higher is generally considered good and can help you qualify for loans at favorable terms.\n"
"3.Annual income: 6 lakh This is your yearly income before taxes and other deductions.\n"
" Lenders use this information to assess your ability to repay a loan. \n"
"A higher income can improve your chances of loan approval.\n"
"4.Debt-to-income ratio: More than 40% Your debt-to-income ratio is the percentage of your monthly income that goes toward paying debts.\n"
"A ratio of more than 40% indicates that a significant portion of your income is already allocated to debt repayment, \n"
"which could affect your ability to take on additional debt."))
        self.pushButton.setText(_translate("dec", "Agree"))

    def check(self, checked):
        if checked:
            self.pushButton.setVisible(True)
        else:
            self.pushButton.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dec = QtWidgets.QMainWindow()
    ui = Ui_dec()
    ui.setupUi(dec)
    dec.show()
    sys.exit(app.exec_())
