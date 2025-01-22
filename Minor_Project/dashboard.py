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
        dashBoard.resize(496, 287)
        self.centralwidget = QtWidgets.QWidget(dashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(340, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setUnderline(True)
        self.email.setFont(font)
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.email.setMouseTracking(False)
        self.email.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.email.setStyleSheet("color: rgb(0, 85, 255);")
        self.email.setObjectName("email")
        self.email_2 = QtWidgets.QLabel(self.centralwidget)
        self.email_2.setGeometry(QtCore.QRect(280, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setUnderline(False)
        self.email_2.setFont(font)
        self.email_2.setMouseTracking(False)
        self.email_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.email_2.setObjectName("email_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 60, 171, 111))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        dashBoard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashBoard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Items = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Items.setObjectName("menuAdd_Items")
        self.menuBook = QtWidgets.QMenu(self.menubar)
        self.menuBook.setObjectName("menuBook")
        self.menuActivities = QtWidgets.QMenu(self.menubar)
        self.menuActivities.setObjectName("menuActivities")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.report = QtWidgets.QMenu(self.menuReport)
        self.report.setObjectName("report")
        self.menuIssue = QtWidgets.QMenu(self.menuReport)
        self.menuIssue.setObjectName("menuIssue")
        self.menuReturn = QtWidgets.QMenu(self.menuReport)
        self.menuReturn.setObjectName("menuReturn")
        self.menuFine = QtWidgets.QMenu(self.menuReport)
        self.menuFine.setObjectName("menuFine")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAdd_user = QtWidgets.QMenu(self.menubar)
        self.menuAdd_user.setObjectName("menuAdd_user")
        dashBoard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dashBoard)
        self.statusbar.setObjectName("statusbar")
        dashBoard.setStatusBar(self.statusbar)
        self.addItems = QtWidgets.QAction(dashBoard)
        self.addItems.setObjectName("addItems")
        self.actionCourse = QtWidgets.QAction(dashBoard)
        self.actionCourse.setObjectName("actionCourse")
        self.actionDepartment = QtWidgets.QAction(dashBoard)
        self.actionDepartment.setObjectName("actionDepartment")
        self.book = QtWidgets.QAction(dashBoard)
        self.book.setObjectName("book")
        self.actionPurchase = QtWidgets.QAction(dashBoard)
        self.actionPurchase.setObjectName("actionPurchase")
        self.activities = QtWidgets.QAction(dashBoard)
        self.activities.setObjectName("activities")
        self.actionIssue_aa_book = QtWidgets.QAction(dashBoard)
        self.actionIssue_aa_book.setObjectName("actionIssue_aa_book")
        self.actionReturn_book = QtWidgets.QAction(dashBoard)
        self.actionReturn_book.setObjectName("actionReturn_book")
        self.actionAll = QtWidgets.QAction(dashBoard)
        self.actionAll.setObjectName("actionAll")
        self.actionMonthly = QtWidgets.QAction(dashBoard)
        self.actionMonthly.setObjectName("actionMonthly")
        self.actionAll_2 = QtWidgets.QAction(dashBoard)
        self.actionAll_2.setObjectName("actionAll_2")
        self.actionMonthly_2 = QtWidgets.QAction(dashBoard)
        self.actionMonthly_2.setObjectName("actionMonthly_2")
        self.actionStudent_wise = QtWidgets.QAction(dashBoard)
        self.actionStudent_wise.setObjectName("actionStudent_wise")
        self.actionAll_3 = QtWidgets.QAction(dashBoard)
        self.actionAll_3.setObjectName("actionAll_3")
        self.actionMonthly_3 = QtWidgets.QAction(dashBoard)
        self.actionMonthly_3.setObjectName("actionMonthly_3")
        self.actionAll_4 = QtWidgets.QAction(dashBoard)
        self.actionAll_4.setObjectName("actionAll_4")
        self.actionMonthly_4 = QtWidgets.QAction(dashBoard)
        self.actionMonthly_4.setObjectName("actionMonthly_4")
        self.actionStudent = QtWidgets.QAction(dashBoard)
        self.actionStudent.setObjectName("actionStudent")
        self.settings = QtWidgets.QAction(dashBoard)
        self.settings.setObjectName("settings")
        self.actionProfile = QtWidgets.QAction(dashBoard)
        self.actionProfile.setObjectName("actionProfile")
        self.actionLogout = QtWidgets.QAction(dashBoard)
        self.actionLogout.setObjectName("actionLogout")
        self.addUser = QtWidgets.QAction(dashBoard)
        self.addUser.setObjectName("addUser")
        self.actionStudent_2 = QtWidgets.QAction(dashBoard)
        self.actionStudent_2.setObjectName("actionStudent_2")
        self.actionBook_Stock = QtWidgets.QAction(dashBoard)
        self.actionBook_Stock.setObjectName("actionBook_Stock")
        self.menuAdd_Items.addAction(self.addItems)
        self.menuAdd_Items.addAction(self.actionCourse)
        self.menuAdd_Items.addAction(self.actionDepartment)
        self.menuBook.addAction(self.book)
        self.menuBook.addAction(self.actionPurchase)
        self.menuActivities.addAction(self.activities)
        self.menuActivities.addAction(self.actionIssue_aa_book)
        self.menuActivities.addAction(self.actionReturn_book)
        self.report.addAction(self.actionAll)
        self.report.addAction(self.actionMonthly)
        self.menuIssue.addAction(self.actionAll_2)
        self.menuIssue.addAction(self.actionMonthly_2)
        self.menuReturn.addAction(self.actionAll_3)
        self.menuReturn.addAction(self.actionMonthly_3)
        self.menuFine.addAction(self.actionAll_4)
        self.menuFine.addAction(self.actionMonthly_4)
        self.menuReport.addAction(self.report.menuAction())
        self.menuReport.addAction(self.menuIssue.menuAction())
        self.menuReport.addAction(self.menuReturn.menuAction())
        self.menuReport.addAction(self.menuFine.menuAction())
        self.menuReport.addAction(self.actionStudent)
        self.menuReport.addAction(self.actionBook_Stock)
        self.menuSettings.addAction(self.settings)
        self.menuSettings.addAction(self.actionProfile)
        self.menuAdd_user.addAction(self.addUser)
        self.menuAdd_user.addAction(self.actionStudent_2)
        self.menubar.addAction(self.menuAdd_Items.menuAction())
        self.menubar.addAction(self.menuAdd_user.menuAction())
        self.menubar.addAction(self.menuBook.menuAction())
        self.menubar.addAction(self.menuActivities.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(dashBoard)
        QtCore.QMetaObject.connectSlotsByName(dashBoard)

        # self.val = "Welcome, " + self.name
        # self.email.setText("hello",self.name)
        # self.email.setText(self.val)
        self.menubar.triggered[QtWidgets.QAction].connect(self.menu)
        self.std.clicked.connect(self.addSTD)
        self.stf.clicked.connect(self.addSTF)
        self.listBooks.clicked.connect(self.listOfBooks)
        self.retBooks.clicked.connect(self.retB)

    def retranslateUi(self, dashBoard):
        _translate = QtCore.QCoreApplication.translate
        dashBoard.setWindowTitle(_translate("dashBoard", "MainWindow"))
        self.email.setText(_translate("dashBoard", "abc@gmail.com"))
        self.email_2.setText(_translate("dashBoard", "Welcome,"))
        self.label.setText(_translate("dashBoard", "Library Dashboard"))
        self.menuAdd_Items.setTitle(_translate("dashBoard", "Add Items"))
        self.menuBook.setTitle(_translate("dashBoard", "Book"))
        self.menuActivities.setTitle(_translate("dashBoard", "Activities"))
        self.menuReport.setTitle(_translate("dashBoard", "Report"))
        self.report.setTitle(_translate("dashBoard", "Purchase"))
        self.menuIssue.setTitle(_translate("dashBoard", "Issue"))
        self.menuReturn.setTitle(_translate("dashBoard", "Return"))
        self.menuFine.setTitle(_translate("dashBoard", "Fine"))
        self.menuSettings.setTitle(_translate("dashBoard", "Settings"))
        self.menuAdd_user.setTitle(_translate("dashBoard", "Add user"))
        self.addItems.setText(_translate("dashBoard", "Subject"))
        self.actionCourse.setText(_translate("dashBoard", "Course"))
        self.actionDepartment.setText(_translate("dashBoard", "Department"))
        self.book.setText(_translate("dashBoard", "Add"))
        self.actionPurchase.setText(_translate("dashBoard", "Purchase"))
        self.activities.setText(_translate("dashBoard", "Book request"))
        self.actionIssue_aa_book.setText(_translate("dashBoard", "Issue a book"))
        self.actionReturn_book.setText(_translate("dashBoard", "Return book"))
        self.actionAll.setText(_translate("dashBoard", "All purchase"))
        self.actionMonthly.setText(_translate("dashBoard", "Monthly purchase"))
        self.actionAll_2.setText(_translate("dashBoard", "All issue"))
        self.actionMonthly_2.setText(_translate("dashBoard", "Monthly issue"))
        self.actionStudent_wise.setText(_translate("dashBoard", "Student wise"))
        self.actionAll_3.setText(_translate("dashBoard", "All return"))
        self.actionMonthly_3.setText(_translate("dashBoard", "Monthly return"))
        self.actionAll_4.setText(_translate("dashBoard", "All fine"))
        self.actionMonthly_4.setText(_translate("dashBoard", "Monthly fine"))
        self.actionStudent.setText(_translate("dashBoard", "Student Report"))
        self.settings.setText(_translate("dashBoard", "Change Password"))
        self.actionProfile.setText(_translate("dashBoard", "Profile"))
        self.actionLogout.setText(_translate("dashBoard", "Logout"))
        self.addUser.setText(_translate("dashBoard", "Librarian"))
        self.actionStudent_2.setText(_translate("dashBoard", "Student"))
        self.actionBook_Stock.setText(_translate("dashBoard", "Book Stock"))

    def menu(self,action):
        txt = (action.text())
        
        # if txt == "Subject":
        #     self.subject = QtWidgets.QMainWindow()
        #     self.ui = Ui_subject()
        #     self.ui.setupUi(self.subject)
        #     self.subject.show()
        # if txt == "Course":
        #     self.coursePage = QtWidgets.QMainWindow()
        #     self.ui = Ui_coursePage()
        #     self.ui.setupUi(self.coursePage)
        #     self.coursePage.show()
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashBoard = QtWidgets.QMainWindow()
    ui = Ui_dashBoard()
    ui.setupUi(dashBoard)
    dashBoard.show()
    sys.exit(app.exec_())
