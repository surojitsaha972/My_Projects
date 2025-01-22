# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courseEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_CourseEdit(object):
    def __init__(self,c):
        self.cName=c
    def setupUi(self, CourseEdit):
        CourseEdit.setObjectName("CourseEdit")
        CourseEdit.resize(800, 575)
        self.centralwidget = QtWidgets.QWidget(CourseEdit)
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
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.courseName = QtWidgets.QLineEdit(self.frame_2)
        self.courseName.setMinimumSize(QtCore.QSize(300, 0))
        self.courseName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.courseName.setObjectName("courseName")
        self.horizontalLayout.addWidget(self.courseName)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.update = QtWidgets.QPushButton(self.frame_3)
        self.update.setObjectName("update")
        self.horizontalLayout_2.addWidget(self.update)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        CourseEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CourseEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CourseEdit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CourseEdit)
        self.statusbar.setObjectName("statusbar")
        CourseEdit.setStatusBar(self.statusbar)

        self.retranslateUi(CourseEdit)
        QtCore.QMetaObject.connectSlotsByName(CourseEdit)

        self.courseName.setText(self.cName)
        self.update.clicked.connect(self.courseUP)
        self.update.clicked.connect(CourseEdit.close)

    def retranslateUi(self, CourseEdit):
        _translate = QtCore.QCoreApplication.translate
        CourseEdit.setWindowTitle(_translate("CourseEdit", "Course Edit"))
        self.label.setText(_translate("CourseEdit", "Course Edit"))
        self.label_2.setText(_translate("CourseEdit", "New Course Name"))
        self.update.setText(_translate("CourseEdit", "Update"))

    def courseUP(self):
        c = self.courseName.text()
        if c=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Fields cann't be empty")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec_()
        else:
            con = sqlite3.connect("projectDB.db")
            cur = con.cursor()
            up = "update Course set CourseName = ? where CourseName= ?"
            cur.execute(up,(c,self.cName))
            con.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("One row updated")
            msg.setWindowTitle("Ok")
            msg.show()
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CourseEdit = QtWidgets.QMainWindow()
    ui = Ui_CourseEdit()
    ui.setupUi(CourseEdit)
    CourseEdit.show()
    sys.exit(app.exec_())
