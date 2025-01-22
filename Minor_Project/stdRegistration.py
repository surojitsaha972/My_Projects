from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
import re

class Ui_stdReg(object):
    def setupUi(self, stdReg):
        stdReg.setObjectName("stdReg")
        stdReg.resize(887, 730)
        self.centralwidget = QtWidgets.QWidget(stdReg)
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
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name = QtWidgets.QLineEdit(self.frame_2)
        self.name.setMinimumSize(QtCore.QSize(226, 0))
        self.name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.name.setObjectName("name")
        self.horizontalLayout_2.addWidget(self.name)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.email = QtWidgets.QLineEdit(self.frame_3)
        self.email.setMinimumSize(QtCore.QSize(226, 0))
        self.email.setMaximumSize(QtCore.QSize(16777215, 30))
        self.email.setObjectName("email")
        self.horizontalLayout_3.addWidget(self.email)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.mobile = QtWidgets.QLineEdit(self.frame_4)
        self.mobile.setMinimumSize(QtCore.QSize(226, 0))
        self.mobile.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mobile.setObjectName("mobile")
        self.horizontalLayout_4.addWidget(self.mobile)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setMinimumSize(QtCore.QSize(89, 0))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.male = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.male.setFont(font)
        self.male.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.male.setObjectName("male")
        self.horizontalLayout_5.addWidget(self.male)
        self.female = QtWidgets.QRadioButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.female.setFont(font)
        self.female.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.female.setObjectName("female")
        self.horizontalLayout_5.addWidget(self.female)
        self.verticalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.course = QtWidgets.QComboBox(self.frame_9)
        self.course.setMinimumSize(QtCore.QSize(115, 0))
        self.course.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MoolBoran")
        font.setPointSize(16)
        self.course.setFont(font)
        self.course.setObjectName("course")
        self.course.addItem("")
        self.course.setItemText(0, "")
        self.horizontalLayout_6.addWidget(self.course)
        self.verticalLayout.addWidget(self.frame_9, 0, QtCore.Qt.AlignHCenter)
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.dept = QtWidgets.QComboBox(self.frame_10)
        self.dept.setMinimumSize(QtCore.QSize(115, 0))
        self.dept.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MoolBoran")
        font.setPointSize(16)
        self.dept.setFont(font)
        self.dept.setObjectName("dept")
        self.dept.addItem("")
        self.dept.setItemText(0, "")
        self.horizontalLayout_7.addWidget(self.dept)
        self.verticalLayout.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.sem = QtWidgets.QComboBox(self.frame_11)
        self.sem.setMinimumSize(QtCore.QSize(115, 0))
        self.sem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MoolBoran")
        font.setPointSize(16)
        self.sem.setFont(font)
        self.sem.setObjectName("sem")
        self.sem.addItem("")
        self.sem.setItemText(0, "")
        self.horizontalLayout_8.addWidget(self.sem)
        self.verticalLayout.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add = QtWidgets.QPushButton(self.frame_12)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setObjectName("add")
        self.verticalLayout_2.addWidget(self.add)
        self.verticalLayout.addWidget(self.frame_12, 0, QtCore.Qt.AlignHCenter)
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stdTable = QtWidgets.QTableWidget(self.frame_13)
        self.stdTable.setMinimumSize(QtCore.QSize(840, 0))
        self.stdTable.setObjectName("stdTable")
        self.stdTable.setColumnCount(8)
        self.stdTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.stdTable.setHorizontalHeaderItem(7, item)
        self.verticalLayout_3.addWidget(self.stdTable)
        self.verticalLayout.addWidget(self.frame_13, 0, QtCore.Qt.AlignHCenter)
        stdReg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(stdReg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 21))
        self.menubar.setObjectName("menubar")
        stdReg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(stdReg)
        self.statusbar.setObjectName("statusbar")
        stdReg.setStatusBar(self.statusbar)

        self.retranslateUi(stdReg)
        QtCore.QMetaObject.connectSlotsByName(stdReg)

        self.add.clicked.connect(self.addStd)
        self.courseName()
        self.deptName()
        self.semister()
        self.showItems()

    def retranslateUi(self, stdReg):
        _translate = QtCore.QCoreApplication.translate
        stdReg.setWindowTitle(_translate("stdReg", "Student Registration"))
        self.label.setText(_translate("stdReg", "Student Registration"))
        self.label_2.setText(_translate("stdReg", "Name"))
        self.label_4.setText(_translate("stdReg", "Email"))
        self.label_5.setText(_translate("stdReg", "Mobile No"))
        self.label_6.setText(_translate("stdReg", "Gender"))
        self.male.setText(_translate("stdReg", "Male"))
        self.female.setText(_translate("stdReg", "Female"))
        self.label_7.setText(_translate("stdReg", "Course"))
        self.label_8.setText(_translate("stdReg", "Department"))
        self.label_9.setText(_translate("stdReg", "Semester"))
        self.add.setText(_translate("stdReg", "Add"))
        item = self.stdTable.horizontalHeaderItem(0)
        item.setText(_translate("stdReg", "SID"))
        item = self.stdTable.horizontalHeaderItem(1)
        item.setText(_translate("stdReg", "Name"))
        item = self.stdTable.horizontalHeaderItem(2)
        item.setText(_translate("stdReg", "Mobile"))
        item = self.stdTable.horizontalHeaderItem(3)
        item.setText(_translate("stdReg", "Email"))
        item = self.stdTable.horizontalHeaderItem(4)
        item.setText(_translate("stdReg", "Gender"))
        item = self.stdTable.horizontalHeaderItem(5)
        item.setText(_translate("stdReg", "Course"))
        item = self.stdTable.horizontalHeaderItem(6)
        item.setText(_translate("stdReg", "Department"))
        item = self.stdTable.horizontalHeaderItem(7)
        item.setText(_translate("stdReg", "Semester"))

        
    def addStd(self):
        n= self.name.text()
        e = self.email.text()
        m = str(self.mobile.text())

        c = self.course.currentText()
        d = self.dept.currentText()
        s = self.sem.currentText()
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        cur1 = con.cursor()
        q =  "Select sid from studentReg order by SID desc limit 1"
        cur1.execute(q)
        res = cur1.fetchall()
        sid = res[0][0] + 1
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, e):
            emailValid = 1;
        else:
            emailValid = 0;

        try:

            if self.male.isChecked():
                gen = "Male"
            elif self.female.isChecked():
                gen = "Female"
            
            if n=="" or e== "" or m== "" or c== "" or d== "" or s== "":
            # if len(m) != 10:
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Critical)
            #     msg.setText("Mobile number should be 10 digit")
            #     msg.setWindowTitle("Warning")
            #     msg.show()
            #     msg.exec_()
            # elif m.isnumeric() == "False":
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Critical)
            #     msg.setText("Mobile number should be numeric")
            #     msg.setWindowTitle("Warning")
            #     msg.show()
            #     msg.exec_()
            

            # if self.male.isChecked():
            #     gen = "Male"
            # elif self.female.isChecked():
            #     gen = "Female"



            # c = self.course.currentText()
            # d = self.dept.currentText()
            # s = self.sem.currentText()
            # con = sqlite3.connect("projectDB.db")
            # cur = con.cursor()
            # cur1 = con.cursor()
            # q =  "Select sid from studentReg order by SID desc limit 1"
            # cur1.execute(q)
            # res = cur1.fetchall()
            # sid = res[0][0] + 1
            # l = len(res)+1
            # q= "insert into studentReg values(?,?,?,?,?,?,?,?)"
            # cur.execute(q,(sid,n,m,e,gen,c,d,s))
            # con.commit()
            # self.showItems()
        
            # if n!="" and e!= "" and m!= "" and c!= "" and d!= "" and s!= "":
            #     # msg = QMessageBox()
            #     # msg.setIcon(QMessageBox.Critical)
            #     # msg.setText("Field cann't be empty")
            #     # msg.setWindowTitle("Warning")
            #     # msg.show()
            #     # msg.exec_()

            #     q= "insert into studentReg values(?,?,?,?,?,?,?,?)"
            #     cur.execute(q,(sid,n,m,e,gen,c,d,s))
            #     con.commit()
 
                if n=="": 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Name field cann't be empty")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()

                # elif e=="" or e!="":
                elif e=="":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Email field cann't be empty")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()
                    # if re.fullmatch(regex, e):
                    #     pass
                    # else:
                    #     msg = QMessageBox()
                    #     msg.setIcon(QMessageBox.Critical)
                    #     msg.setText("Enter valid email address")
                    #     msg.setWindowTitle("Warning")
                    #     msg.show()
                    #     msg.exec_()

                elif e!="" and emailValid == 0:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Enter valid email address")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()
            
                elif m=="":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Moblie number field cann't be empty")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()

                elif m!="" and len(m) != 10:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Moblie number should be 10 digit")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()

                elif c =="":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Select course name")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()
                
                elif d =="":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Select department name")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()

                elif s =="":
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Select Semister")
                    msg.setWindowTitle("Warning")
                    msg.show()
                    msg.exec_()

                # if n!="" and e!= "" and m!= "" and c!= "" and d!= "" and s!= "":
                    # msg = QMessageBox()
                    # msg.setIcon(QMessageBox.Critical)
                    # msg.setText("Field cann't be empty")
                    # msg.setWindowTitle("Warning")
                    # msg.show()
                    # msg.exec_()
                    # q= "insert into studentReg values(?,?,?,?,?,?,?,?)"
                    # cur.execute(q,(sid,n,m,e,gen,c,d,s))
                    # con.commit()
                    # # print(sid,n,m,e,gen,c,d,s)


                    # msg = QMessageBox()
                    # msg.setIcon(QMessageBox.Information)
                    # msg.setText("One student added")
                    # msg.setWindowTitle("Add successful")
                    # msg.show()
                    # msg.exec_()

                    # self.showItems()
            else:
                q= "insert into studentReg values(?,?,?,?,?,?,?,?)"
                cur.execute(q,(sid,n,m,e,gen,c,d,s))
                con.commit()
                # print(sid,n,m,e,gen,c,d,s)


                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("One student added")
                msg.setWindowTitle("Add successful")
                msg.show()
                msg.exec_()

                self.showItems()

        except sqlite3.IntegrityError:
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Critical)
            # msg.setText("Enter email")
            # msg.setWindowTitle("Warning")
            # msg.show()
            # msg.exec_()
            if e=="":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Email field cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
            
            elif m=="":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Moblie number field cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()

        except UnboundLocalError:
            if n=="": 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Name field cann't be empty")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Select the Gender")
                msg.setWindowTitle("Warning")
                msg.show()
                msg.exec_()
        
        

        

    def courseName(self):
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q1 = "select * from Course"
        cur.execute(q1)
        c = cur.fetchall()
        for i in c:
            self.course.addItem(i[0])
    
    def deptName(self):
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q1 = "select * from department"
        cur.execute(q1)
        c = cur.fetchall()
        for i in c:
            self.dept.addItem(i[0])
    
    def semister(self):
        for i in range(1,9):
            self.sem.addItem(str(i))

    def showItems(self):
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q =  "Select * from studentReg"
        cur.execute(q)
        res = cur.fetchall()
        self.stdTable.setRowCount(0)
        for i in res:
            rc = self.stdTable.rowCount()
            self.stdTable.insertRow(rc)
            self.stdTable.setItem(rc,0,QtWidgets.QTableWidgetItem(str(i[0])))
            self.stdTable.setItem(rc,1,QtWidgets.QTableWidgetItem(i[1]))
            self.stdTable.setItem(rc,2,QtWidgets.QTableWidgetItem(i[2]))
            self.stdTable.setItem(rc,3,QtWidgets.QTableWidgetItem(i[3]))
            self.stdTable.setItem(rc,4,QtWidgets.QTableWidgetItem(i[4]))
            self.stdTable.setItem(rc,5,QtWidgets.QTableWidgetItem(i[5]))
            self.stdTable.setItem(rc,6,QtWidgets.QTableWidgetItem(i[6]))
            self.stdTable.setItem(rc,7,QtWidgets.QTableWidgetItem(i[7]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    stdReg = QtWidgets.QMainWindow()
    ui = Ui_stdReg()
    ui.setupUi(stdReg)
    stdReg.show()
    sys.exit(app.exec_())
