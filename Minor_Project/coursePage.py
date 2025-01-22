from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from courseEdit import *

class Ui_coursePage(object):
    def setupUi(self, coursePage):
        coursePage.setObjectName("coursePage")
        coursePage.resize(791, 573)
        self.centralwidget = QtWidgets.QWidget(coursePage)
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
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
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
        self.courseName.setMinimumSize(QtCore.QSize(150, 0))
        self.courseName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.courseName.setObjectName("courseName")
        self.horizontalLayout.addWidget(self.courseName)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add = QtWidgets.QPushButton(self.frame_3)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setObjectName("add")
        self.horizontalLayout_2.addWidget(self.add)
        self.verticalLayout_4.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.courseTable = QtWidgets.QTableWidget(self.frame_4)
        self.courseTable.setMaximumSize(QtCore.QSize(120, 150))
        self.courseTable.setObjectName("courseTable")
        self.courseTable.setColumnCount(1)
        self.courseTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.courseTable.setHorizontalHeaderItem(0, item)
        self.verticalLayout_3.addWidget(self.courseTable, 0, QtCore.Qt.AlignHCenter)
        self.edit = QtWidgets.QPushButton(self.frame_4)
        self.edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit.setObjectName("edit")
        self.verticalLayout_3.addWidget(self.edit, 0, QtCore.Qt.AlignHCenter)
        self.remove = QtWidgets.QPushButton(self.frame_4)
        self.remove.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove.setObjectName("remove")
        self.verticalLayout_3.addWidget(self.remove, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_4)
        coursePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(coursePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        coursePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(coursePage)
        self.statusbar.setObjectName("statusbar")
        coursePage.setStatusBar(self.statusbar)

        self.retranslateUi(coursePage)
        QtCore.QMetaObject.connectSlotsByName(coursePage)

        self.add.clicked.connect(self.addCourse)
        self.remove.clicked.connect(self.removeCourse)
        self.edit.clicked.connect(self.editCourse)
        self.edit.clicked.connect(coursePage.close)
        self.showCourse()

    def retranslateUi(self, coursePage):
        _translate = QtCore.QCoreApplication.translate
        coursePage.setWindowTitle(_translate("coursePage", "Add course"))
        self.label.setText(_translate("coursePage", "Course"))
        self.label_2.setText(_translate("coursePage", "Course Name"))
        self.add.setText(_translate("coursePage", "Add"))
        item = self.courseTable.horizontalHeaderItem(0)
        item.setText(_translate("coursePage", "Course Name"))
        self.edit.setText(_translate("coursePage", "Edit"))
        self.remove.setText(_translate("coursePage", "Remove"))

    def addCourse(self):
        c = self.courseName.text()
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        try:
            if c == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Fields cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
            else:
                q = "insert into Course values (?)"
                cur.execute(q,(c,))
                con.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Course inserted")
                msg.setWindowTitle("Insert")
                msg.show()
                msg.exec_()
                self.showCourse()

        except sqlite3.IntegrityError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Course name already exists")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()

    def showCourse(self):
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q =  "Select * from Course"
        cur.execute(q)
        res = cur.fetchall()
        self.courseTable.setRowCount(0)
        for i in res:
            rc = self.courseTable.rowCount()
            self.courseTable.insertRow(rc)
            self.courseTable.setItem(rc,0,QtWidgets.QTableWidgetItem(i[0]))
    
    def removeCourse(self):
        # Delete from the table
        del_i = self.courseTable.currentIndex()
        rw = del_i.row()
        self.courseTable.removeRow(rw)
        
        # connect to the database
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        cur1 = con.cursor()
        
        # Select the particular row
        q = "select * from Course limit ?,1"
        cur.execute(q,(rw,))
        res = cur.fetchall()
        c = res[0]

        # Delete from DB
        if rw==-1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Select any row")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        else:
            nq = "delete from Course where CourseName=?"
            cur1.execute(nq,c)
            con.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("One row is deleted")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
            self.courseName.setText(" ")

    def editCourse(self):
        # c = self.courseName.text()
        i = self.courseTable.currentIndex()
        rw = i.row()
        
        # connect to the database
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        
        # Select the particular row
        q = "select * from Course limit ?,1"
        cur.execute(q,(rw,))
        res = cur.fetchall()
        cName = res[0][0]
        
        # TRANSFER VALUE TO THE NEXT PAGE
        if rw == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Select any row")
            msg.setWindowTitle("Warning")
            msg.show()
            msg.exec_()
        else:
            # self.courseName.setText(r)
            self.CourseEdit = QtWidgets.QMainWindow()
            self.ui = Ui_CourseEdit(cName)
            self.ui.setupUi(self.CourseEdit)
            self.CourseEdit.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    coursePage = QtWidgets.QMainWindow()
    ui = Ui_coursePage()
    ui.setupUi(coursePage)
    coursePage.show()
    sys.exit(app.exec_())
