from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
# from reportPurchase import *
from fpdf import FPDF

class Ui_purchaseReport(object):
    def setupUi(self, purchaseReport):
        purchaseReport.setObjectName("purchaseReport")
        purchaseReport.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(purchaseReport)
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
        self.frame_2.setMinimumSize(QtCore.QSize(860, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.table = QtWidgets.QTableWidget(self.frame_2)
        self.table.setObjectName("table")
        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        self.verticalLayout_4.addWidget(self.table)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pdf = QtWidgets.QPushButton(self.frame_3)
        self.pdf.setMinimumSize(QtCore.QSize(97, 39))
        self.pdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pdf.setObjectName("pdf")
        self.verticalLayout_3.addWidget(self.pdf)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        purchaseReport.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(purchaseReport)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        purchaseReport.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(purchaseReport)
        self.statusbar.setObjectName("statusbar")
        purchaseReport.setStatusBar(self.statusbar)

        self.retranslateUi(purchaseReport)
        QtCore.QMetaObject.connectSlotsByName(purchaseReport)

        self.purReport()
        self.pdf.clicked.connect(self.repPDF)
        self.pdf.clicked.connect(purchaseReport.close)

    def retranslateUi(self, purchaseReport):
        _translate = QtCore.QCoreApplication.translate
        purchaseReport.setWindowTitle(_translate("purchaseReport", "Purchase Report"))
        self.label.setText(_translate("purchaseReport", "Purchase Report"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("purchaseReport", "SubjectName"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("purchaseReport", "BookName"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("purchaseReport", "AuthorName"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("purchaseReport", "Edition"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("purchaseReport", "Quantity"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("purchaseReport", "Price"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("purchaseReport", "Date"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("purchaseReport", "Time"))
        self.pdf.setText(_translate("purchaseReport", "Generate PDF"))

    def purReport(self):
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q = "select * from purchaseBook"
        cur.execute(q)
        res= cur.fetchall()
        if res == []:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Purchase not done yet")
            msg.setWindowTitle("Invalid")
            msg.show()
            msg.exec_()    
        else:
            self.table.setRowCount(0)
            for i in res:
                # print(i)
                rc = self.table.rowCount()
                self.table.insertRow(rc)
                self.table.setItem(rc,0,QtWidgets.QTableWidgetItem(i[0]))
                self.table.setItem(rc,1,QtWidgets.QTableWidgetItem(i[1]))
                self.table.setItem(rc,2,QtWidgets.QTableWidgetItem(i[2]))
                self.table.setItem(rc,3,QtWidgets.QTableWidgetItem(i[3]))
                self.table.setItem(rc,4,QtWidgets.QTableWidgetItem(str(i[4])))
                self.table.setItem(rc,5,QtWidgets.QTableWidgetItem(str(i[5])))
                self.table.setItem(rc,6,QtWidgets.QTableWidgetItem(i[6]))
                self.table.setItem(rc,7,QtWidgets.QTableWidgetItem(i[7]))

    def repPDF(self):
        spacing=4    
        con = sqlite3.connect("projectDB.db")
        cur = con.cursor()
        q = "select * from purchaseBook"
        cur.execute(q)
        res= cur.fetchall()
        l = []
        # if res == l:
        # data = [('PYTHON/001', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-11', '2023-07-15', '2023-07-27', 'F101'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-27', 'NULL'), ('PYTHON/003', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', '2023-07-25', 'NULL'), ('JAVA/001','Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-08-26', '2023-07-27', 'NULL'), ('JAVA/002', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-20', '2023-07-26', '2023-07-27', 'F103'), ('gf', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('ghg', 'Pyhton', 'The ABC of Python', 'Souvik Karmakar', '2023-07-25', '2023-08-08', 'NULL', 'NULL'), ('abv', 'Java', 'The XYZ of Java', 'Souvik Karmakar', '2023-07-26', '2023-08-08', 'NULL', 'NULL')]
        data = [[str(i) for i in j] for j in res]
        # data.insert(0,('A','b','c','d','e','f','g','h'))
        data.insert(0,('SubjectName','BookName','AuthorName','Edition','Quantity','Price','Date','Time'))
        pdf = FPDF('L','mm','A4')
        pdf.set_font('helvetica','B',9)
        pdf.add_page()

        col_width = pdf.w / 8.5
        row_height = pdf.font_size
        for row in data:
            for item in row:
                pdf.cell(col_width, row_height*spacing, txt=item, border=2)
            pdf.ln(row_height*spacing)
            
        pdf.output('simple_table_3.pdf')

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("PDF has download!")
        msg.setWindowTitle("PDF")
        msg.show()
        msg.exec_() 

        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("Table is empty")
        #     msg.setWindowTitle("PDF")
        #     msg.show()
        #     msg.exec_()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    purchaseReport = QtWidgets.QMainWindow()
    ui = Ui_purchaseReport()
    ui.setupUi(purchaseReport)
    purchaseReport.show()
    sys.exit(app.exec_())
