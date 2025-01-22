from PyQt5 import QtCore, QtGui, QtWidgets
from addSubject import *
from coursePage import *
from departmentPage import *

from librarianRegistrartion import *
from stdRegistration import *

from addBook import *
from purchaseBook import *

from bookRequest import *
from pendingRequest import *
from returnBook import *

from reportPurchase import *
from reportPurchaseMonth import *
from reportIssueBook import *
from reportIssueBookMonth import *
from reportReturnBook import *
from reportReturnBookMonth import *
from reportFine import *
from reportFineMonth import *
from reportSID import *
from reportBookStock import *

from changePassword import *
from profile import *

class Ui_dashBoard(object):
    def __init__(self,e,n,m):
        self.mail = e
        self.name = n
        self.mobile = m
    def setupUi(self, dashBoard):
        dashBoard.setObjectName("dashBoard")
        dashBoard.resize(863, 601)
        self.centralwidget = QtWidgets.QWidget(dashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.std = QtWidgets.QPushButton(self.frame)
        self.std.setMaximumSize(QtCore.QSize(16777215, 50))
        self.std.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.std.setObjectName("std")
        self.verticalLayout.addWidget(self.std)
        self.stf = QtWidgets.QPushButton(self.frame)
        self.stf.setMaximumSize(QtCore.QSize(16777215, 50))
        self.stf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stf.setObjectName("stf")
        self.verticalLayout.addWidget(self.stf)
        self.bkreq = QtWidgets.QPushButton(self.frame)
        self.bkreq.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bkreq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bkreq.setObjectName("bkreq")
        self.verticalLayout.addWidget(self.bkreq)
        self.listBooks = QtWidgets.QPushButton(self.frame)
        self.listBooks.setMaximumSize(QtCore.QSize(16777215, 50))
        self.listBooks.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listBooks.setObjectName("listBooks")
        self.verticalLayout.addWidget(self.listBooks)
        self.retBooks = QtWidgets.QPushButton(self.frame)
        self.retBooks.setMaximumSize(QtCore.QSize(16777215, 50))
        self.retBooks.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retBooks.setObjectName("retBooks")
        self.verticalLayout.addWidget(self.retBooks)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        dashBoard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashBoard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Items = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Items.setObjectName("menuAdd_Items")
        self.menuBook = QtWidgets.QMenu(self.menubar)
        self.menuBook.setObjectName("menuBook")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menuPurchase = QtWidgets.QMenu(self.menuReport)
        self.menuPurchase.setObjectName("menuPurchase")
        self.menuIssue = QtWidgets.QMenu(self.menuReport)
        self.menuIssue.setObjectName("menuIssue")
        self.menuReturn = QtWidgets.QMenu(self.menuReport)
        self.menuReturn.setObjectName("menuReturn")
        self.menuFine = QtWidgets.QMenu(self.menuReport)
        self.menuFine.setObjectName("menuFine")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        dashBoard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dashBoard)
        self.statusbar.setObjectName("statusbar")
        dashBoard.setStatusBar(self.statusbar)
        self.actionSubject = QtWidgets.QAction(dashBoard)
        self.actionSubject.setObjectName("actionSubject")
        self.actionCourse = QtWidgets.QAction(dashBoard)
        self.actionCourse.setObjectName("actionCourse")
        self.actionDepartment = QtWidgets.QAction(dashBoard)
        self.actionDepartment.setObjectName("actionDepartment")
        self.actionAdd = QtWidgets.QAction(dashBoard)
        self.actionAdd.setObjectName("actionAdd")
        self.actionPurchase = QtWidgets.QAction(dashBoard)
        self.actionPurchase.setObjectName("actionPurchase")
        self.actionAll_purchase = QtWidgets.QAction(dashBoard)
        self.actionAll_purchase.setObjectName("actionAll_purchase")
        self.actionMonthly_purchase = QtWidgets.QAction(dashBoard)
        self.actionMonthly_purchase.setObjectName("actionMonthly_purchase")
        self.actionAll_issue = QtWidgets.QAction(dashBoard)
        self.actionAll_issue.setObjectName("actionAll_issue")
        self.actionMonthly_issue = QtWidgets.QAction(dashBoard)
        self.actionMonthly_issue.setObjectName("actionMonthly_issue")
        self.actionAll_return = QtWidgets.QAction(dashBoard)
        self.actionAll_return.setObjectName("actionAll_return")
        self.actionMonthly_return = QtWidgets.QAction(dashBoard)
        self.actionMonthly_return.setObjectName("actionMonthly_return")
        self.actionAll_fine = QtWidgets.QAction(dashBoard)
        self.actionAll_fine.setObjectName("actionAll_fine")
        self.actionMonthly_fine = QtWidgets.QAction(dashBoard)
        self.actionMonthly_fine.setObjectName("actionMonthly_fine")
        self.actionStudent_Report = QtWidgets.QAction(dashBoard)
        self.actionStudent_Report.setObjectName("actionStudent_Report")
        self.actionBook_Stock = QtWidgets.QAction(dashBoard)
        self.actionBook_Stock.setObjectName("actionBook_Stock")
        self.actionChange_Password = QtWidgets.QAction(dashBoard)
        self.actionChange_Password.setObjectName("actionChange_Password")
        self.actionProfile = QtWidgets.QAction(dashBoard)
        self.actionProfile.setObjectName("actionProfile")
        self.menuAdd_Items.addAction(self.actionSubject)
        self.menuAdd_Items.addAction(self.actionCourse)
        self.menuAdd_Items.addAction(self.actionDepartment)
        self.menuBook.addAction(self.actionAdd)
        self.menuBook.addAction(self.actionPurchase)
        self.menuPurchase.addAction(self.actionAll_purchase)
        self.menuPurchase.addAction(self.actionMonthly_purchase)
        self.menuIssue.addAction(self.actionAll_issue)
        self.menuIssue.addAction(self.actionMonthly_issue)
        self.menuReturn.addAction(self.actionAll_return)
        self.menuReturn.addAction(self.actionMonthly_return)
        self.menuFine.addAction(self.actionAll_fine)
        self.menuFine.addAction(self.actionMonthly_fine)
        self.menuReport.addAction(self.menuPurchase.menuAction())
        self.menuReport.addAction(self.menuIssue.menuAction())
        self.menuReport.addAction(self.menuReturn.menuAction())
        self.menuReport.addAction(self.menuFine.menuAction())
        self.menuReport.addAction(self.actionStudent_Report)
        self.menuReport.addAction(self.actionBook_Stock)
        self.menuSettings.addAction(self.actionChange_Password)
        self.menuSettings.addAction(self.actionProfile)
        self.menubar.addAction(self.menuAdd_Items.menuAction())
        self.menubar.addAction(self.menuBook.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(dashBoard)
        QtCore.QMetaObject.connectSlotsByName(dashBoard)

        self.menubar.triggered[QtWidgets.QAction].connect(self.menu)
        self.std.clicked.connect(self.addSTD)
        self.stf.clicked.connect(self.addSTF)
        self.listBooks.clicked.connect(self.listOfBooks)
        self.retBooks.clicked.connect(self.retB)
        self.bkreq.clicked.connect(self.bookr)

    def retranslateUi(self, dashBoard):
        _translate = QtCore.QCoreApplication.translate
        dashBoard.setWindowTitle(_translate("dashBoard", "Dashboard"))
        self.label.setText(_translate("dashBoard", "Library Dashboard"))
        self.std.setText(_translate("dashBoard", "Add Student"))
        self.stf.setText(_translate("dashBoard", "Add Staff"))
        self.bkreq.setText(_translate("dashBoard", "Book Request"))
        self.listBooks.setText(_translate("dashBoard", "List of Book requests"))
        self.retBooks.setText(_translate("dashBoard", "Return Book"))
        self.menuAdd_Items.setTitle(_translate("dashBoard", "Add Items"))
        self.menuBook.setTitle(_translate("dashBoard", "Book"))
        self.menuReport.setTitle(_translate("dashBoard", "Report"))
        self.menuPurchase.setTitle(_translate("dashBoard", "Purchase"))
        self.menuIssue.setTitle(_translate("dashBoard", "Issue"))
        self.menuReturn.setTitle(_translate("dashBoard", "Return"))
        self.menuFine.setTitle(_translate("dashBoard", "Fine"))
        self.menuSettings.setTitle(_translate("dashBoard", "Settings"))
        self.actionSubject.setText(_translate("dashBoard", "Subject"))
        self.actionCourse.setText(_translate("dashBoard", "Course"))
        self.actionDepartment.setText(_translate("dashBoard", "Department"))
        self.actionAdd.setText(_translate("dashBoard", "Add"))
        self.actionPurchase.setText(_translate("dashBoard", "Purchase"))
        self.actionAll_purchase.setText(_translate("dashBoard", "All purchase"))
        self.actionMonthly_purchase.setText(_translate("dashBoard", "Monthly purchase"))
        self.actionAll_issue.setText(_translate("dashBoard", "All issue"))
        self.actionMonthly_issue.setText(_translate("dashBoard", "Monthly issue"))
        self.actionAll_return.setText(_translate("dashBoard", "All return"))
        self.actionMonthly_return.setText(_translate("dashBoard", "Monthly return"))
        self.actionAll_fine.setText(_translate("dashBoard", "All fine"))
        self.actionMonthly_fine.setText(_translate("dashBoard", "Monthly fine"))
        self.actionStudent_Report.setText(_translate("dashBoard", "Student Report"))
        self.actionBook_Stock.setText(_translate("dashBoard", "Book Stock"))
        self.actionChange_Password.setText(_translate("dashBoard", "Change Password"))
        self.actionProfile.setText(_translate("dashBoard", "Profile"))

    def menu(self,action):
        txt = (action.text())
        
        if txt == "Subject":
            self.subject = QtWidgets.QMainWindow()
            self.ui = Ui_subject()
            self.ui.setupUi(self.subject)
            self.subject.show()
        if txt == "Course":
            self.coursePage = QtWidgets.QMainWindow()
            self.ui = Ui_coursePage()
            self.ui.setupUi(self.coursePage)
            self.coursePage.show()
        if txt == "Department":
            self.department = QtWidgets.QMainWindow()
            self.ui = Ui_department()
            self.ui.setupUi(self.department)
            self.department.show()
        
        if txt == "Librarian":
            self.librarian_registration = QtWidgets.QMainWindow()
            self.ui = Ui_librarian_registration()
            self.ui.setupUi(self.librarian_registration)
            self.librarian_registration.show()
        if txt == "Student":
            self.stdReg = QtWidgets.QMainWindow()
            self.ui = Ui_stdReg()
            self.ui.setupUi(self.stdReg)
            self.stdReg.show()

        if txt == "Add":
            self.book = QtWidgets.QMainWindow()
            self.ui = Ui_book()
            self.ui.setupUi(self.book)
            self.book.show()
        if txt == "Purchase":
            self.purchaseBook = QtWidgets.QMainWindow()
            self.ui = Ui_purchaseBook()
            self.ui.setupUi(self.purchaseBook)
            self.purchaseBook.show()
        
        # if txt == "Book request":
        #     self.bookReq = QtWidgets.QMainWindow()
        #     self.ui = Ui_bookReq()
        #     self.ui.setupUi(self.bookReq)
            # self.bookReq.show()
        # if txt == "Issue a book":
        #     self.pendingReq = QtWidgets.QMainWindow()
        #     self.ui = Ui_pendingReq()
        #     self.ui.setupUi(self.pendingReq)
        #     self.pendingReq.show()
        # if txt == "Return book":
        #     self.returnBook = QtWidgets.QMainWindow()
        #     self.ui = Ui_returnBook()
        #     self.ui.setupUi(self.returnBook)
        #     self.returnBook.show()

        if txt == "All purchase":
            self.purchaseReport = QtWidgets.QMainWindow()
            self.ui = Ui_purchaseReport()
            self.ui.setupUi(self.purchaseReport)
            self.purchaseReport.show()
        if txt == "Monthly purchase":
            self.repPurMonth = QtWidgets.QMainWindow()
            self.ui = Ui_repPurMonth()
            self.ui.setupUi(self.repPurMonth)
            self.repPurMonth.show()
        if txt == "All issue":
            self.issueBook = QtWidgets.QMainWindow()
            self.ui = Ui_issueBook()
            self.ui.setupUi(self.issueBook)
            self.issueBook.show()
        if txt == "Monthly issue":
            self.repbookMon = QtWidgets.QMainWindow()
            self.ui = Ui_repbookMon()
            self.ui.setupUi(self.repbookMon)
            self.repbookMon.show()
        if txt == "All return":
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
        if txt == "Monthly return":
            self.repRetMon = QtWidgets.QMainWindow()
            self.ui = Ui_repRetMon()
            self.ui.setupUi(self.repRetMon)
            self.repRetMon.show()
        if txt == "All fine":
            self.fine = QtWidgets.QMainWindow()
            self.ui = Ui_fine()
            self.ui.setupUi(self.fine)
            self.fine.show()
        if txt == "Monthly fine":
            self.reportFineMon = QtWidgets.QMainWindow()
            self.ui = Ui_reportFineMon()
            self.ui.setupUi(self.reportFineMon)
            self.reportFineMon.show()
        if txt == "Student Report":
            self.sidReport = QtWidgets.QMainWindow()
            self.ui = Ui_sidReport()
            self.ui.setupUi(self.sidReport)
            self.sidReport.show()
        if txt == "Book Stock":
            self.bookStock = QtWidgets.QMainWindow()
            self.ui = Ui_bookStock()
            self.ui.setupUi(self.bookStock)
            self.bookStock.show()



        if txt == "Change Password":
            self.changePa = QtWidgets.QMainWindow()
            self.ui = Ui_changePa(self.mail)
            self.ui.setupUi(self.changePa)
            self.changePa.show()  
        
        if txt == "Profile":
            self.pro = QtWidgets.QMainWindow()
            self.ui = Ui_pro(self.mail,self.name,self.mobile)
            self.ui.setupUi(self.pro)
            self.pro.show()

    def addSTD(self):
        self.stdReg = QtWidgets.QMainWindow()
        self.ui = Ui_stdReg()
        self.ui.setupUi(self.stdReg)
        self.stdReg.show()
    
    def addSTF(self):
        self.librarian_registration = QtWidgets.QMainWindow()
        self.ui = Ui_librarian_registration()
        self.ui.setupUi(self.librarian_registration)
        self.librarian_registration.show()

    def listOfBooks(self):
        self.pendingReq = QtWidgets.QMainWindow()
        self.ui = Ui_pendingReq()
        self.ui.setupUi(self.pendingReq)
        self.pendingReq.show()
    
    def retB(self):
        self.returnBook = QtWidgets.QMainWindow()
        self.ui = Ui_returnBook()
        self.ui.setupUi(self.returnBook)
        self.returnBook.show()
    def bookr(self):
        self.bookReq = QtWidgets.QMainWindow()
        self.ui = Ui_bookReq()
        self.ui.setupUi(self.bookReq)
        self.bookReq.show()

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashBoard = QtWidgets.QMainWindow()
    ui = Ui_dashBoard()
    ui.setupUi(dashBoard)
    dashBoard.show()
    sys.exit(app.exec_())
