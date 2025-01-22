from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_Add_Bank_Name(object):
    def setupUi(self, Add_Bank_Name):
        Add_Bank_Name.setObjectName("Add_Bank_Name")
        Add_Bank_Name.resize(1368, 878)
        Add_Bank_Name.setMinimumSize(QtCore.QSize(1368, 878))
        Add_Bank_Name.setMaximumSize(QtCore.QSize(1368, 878))
        self.centralwidget = QtWidgets.QWidget(Add_Bank_Name)
        self.centralwidget.setObjectName("centralwidget")
        self.bntext = QtWidgets.QLineEdit(self.centralwidget)
        self.bntext.setGeometry(QtCore.QRect(590, 220, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bntext.setFont(font)
        self.bntext.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.bntext.setText("")
        self.bntext.setObjectName("bntext")
        self.insertbut = QtWidgets.QPushButton(self.centralwidget)
        self.insertbut.setGeometry(QtCore.QRect(540, 340, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.insertbut.setFont(font)
        self.insertbut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insertbut.setStyleSheet("\n"
"background-color: rgb(255, 253, 231);\n"
"border-radius:20px;")
        self.insertbut.setObjectName("insertbut")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 60, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        Add_Bank_Name.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Add_Bank_Name)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1368, 27))
        self.menubar.setObjectName("menubar")
        Add_Bank_Name.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Add_Bank_Name)
        self.statusbar.setObjectName("statusbar")
        Add_Bank_Name.setStatusBar(self.statusbar)

        self.insertbut.clicked.connect(self.add)

        self.retranslateUi(Add_Bank_Name)
        QtCore.QMetaObject.connectSlotsByName(Add_Bank_Name)

    def retranslateUi(self, Add_Bank_Name):
        _translate = QtCore.QCoreApplication.translate
        Add_Bank_Name.setWindowTitle(_translate("Add_Bank_Name", "Add_Bank_Nmae"))
        self.insertbut.setText(_translate("Add_Bank_Name", "INSERT"))
        self.label_2.setText(_translate("Add_Bank_Name", "Bank Name:"))
        self.label.setText(_translate("Add_Bank_Name", "Add Bank Name"))

    def add(self):
        br = self.bntext.text().lstrip().rstrip()
        con = sqlite3.connect("UMRS.db")
        cur = con.cursor()
        if br=="":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Empty Data")
                msg.setWindowTitle("Add Bank Name")
                msg.show()
                msg.exec_()
        else:            
                q = "insert into Bank_Name values (?)"
                cur.execute(q,(br,))
                con.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Bank Name is added")
                msg.setWindowTitle("Add Bank Name")
                msg.show()
                msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Bank_Name = QtWidgets.QMainWindow()
    ui = Ui_Add_Bank_Name()
    ui.setupUi(Add_Bank_Name)
    Add_Bank_Name.show()
    sys.exit(app.exec_())
