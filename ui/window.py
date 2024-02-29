from PyQt5.QtWidgets import QMainWindow, QTableView, QLineEdit, QLabel
import sqlite3
from ui.UI_MainWindow import Ui_MainWindow
from bl.inventory import Inventory
from bl.inventory import Medicine
from bl.inventory import Patient


class windowUI():

    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cur = self.con.cursor()
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)       
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

        # LOGIN PAGE
        self.warning = self.main_win.findChild(QLabel, 'warningLabel')
        self.name = self.main_win.findChild(QLineEdit, 'nameInput')
        self.pw = self.main_win.findChild(QLineEdit, 'pwInput')
        self.greeting = self.main_win.findChild(QLabel, 'greetingLabel')

        # REGISTER PAGE
        self.rName = self.main_win.findChild(QLineEdit, 'rNameInput')
        self.rUser = self.main_win.findChild(QLineEdit, 'rUsernameInput')
        self.rPw = self.main_win.findChild(QLineEdit, 'rPwInput')
        self.rButton = self.main_win.findChild(QLineEdit, 'registerButton_2')

        # ADD MEDICINE
        self.amName = self.main_win.findChild(QLineEdit, 'amnameInput')
        self.amPur = self.main_win.findChild(QLineEdit, 'ampurposeInput')
        self.amExp = self.main_win.findChild(QLineEdit, 'amexpInput')
        self.amQty = self.main_win.findChild(QLineEdit, 'amqtyInput')
        self.amCost = self.main_win.findChild(QLineEdit, 'amcostInput')
        self.amWarning = self.main_win.findChild(QLabel, 'amWarningLabel')

        # UPDATE MEDICINE
        self.mID = self.main_win.findChild(QLineEdit, 'umidInput')
        self.umName = self.main_win.findChild(QLineEdit, 'umnameInput')
        self.umPur = self.main_win.findChild(QLineEdit, 'umpurposeInput')
        self.umExp = self.main_win.findChild(QLineEdit, 'umexpInput')
        self.umQty = self.main_win.findChild(QLineEdit, 'umqtyInput')
        self.umCost = self.main_win.findChild(QLineEdit, 'umcostInput')
        self.umWarning = self.main_win.findChild(QLabel, 'umWarningLabel')

        # VIEW MEDICINE PAGE
        self.vmTable = self.main_win.findChild(QTableView, 'vmTableView')

        # ADD PATIENT PAGE
        self.apName = self.main_win.findChild(QLineEdit, 'apnameInput')
        self.apAge = self.main_win.findChild(QLineEdit, 'apageInput')
        self.apGender = self.main_win.findChild(QLineEdit, 'apgenderInput')
        self.apWeight = self.main_win.findChild(QLineEdit, 'apweightInput')
        self.apStatus = self.main_win.findChild(QLineEdit, 'apstatusInput')
        self.apMed = self.main_win.findChild(QLineEdit, 'apmedicineInput')
        self.apRem = self.main_win.findChild(QLineEdit, 'apremarksInput')
        self.apWarning = self.main_win.findChild(QLabel, 'apWarningLabel')

        # UPDATE PATIENT
        self.pID = self.main_win.findChild(QLineEdit, 'upidInput')
        self.upName = self.main_win.findChild(QLineEdit, 'upnameInput')
        self.upAge = self.main_win.findChild(QLineEdit, 'upageInput')
        self.upGender = self.main_win.findChild(QLineEdit, 'upgenderInput')
        self.upWeight = self.main_win.findChild(QLineEdit, 'upweightInput')
        self.upStatus = self.main_win.findChild(QLineEdit, 'upstatusInput')
        self.upMed = self.main_win.findChild(QLineEdit, 'upmedicineInput')
        self.upRem = self.main_win.findChild(QLineEdit, 'upremarksInput')
        self.upWarning = self.main_win.findChild(QLabel, 'upWarningLabel')

        # VIEW PATIENT PAGE
        self.vpTable = self.main_win.findChild(QTableView, 'vpTableView')
        
        self.ui.loginButton.clicked.connect(self.loginClick)
        self.ui.logOutButton.clicked.connect(self.logOutClick)
        self.ui.registerButton.clicked.connect(self.registerClick)
        self.ui.registerButton_2.clicked.connect(self.userRegistered)

        self.ui.amMenuButton.clicked.connect(self.amMenuClick)
        self.ui.addMedicineButton.clicked.connect(self.addMedicineClick)
        self.ui.amReturnButton.clicked.connect(self.menuClick)

        self.ui.umMenuButton.clicked.connect(self.umMenuClick)
        self.ui.updateMedicineButton.clicked.connect(self.updateMedicineClick)
        self.ui.umReturnButton.clicked.connect(self.menuClick)

        self.ui.vmMenuButton.clicked.connect(self.vmMenuClick)
        self.ui.vmReturnButton.clicked.connect(self.menuClick)

        self.ui.apMenuButton.clicked.connect(self.apMenuClick)
        self.ui.addPatientButton.clicked.connect(self.addPatientClick)
        self.ui.apReturnButton.clicked.connect(self.menuClick)

        self.ui.upMenuButton.clicked.connect(self.upMenuClick)
        self.ui.updatePatientButton.clicked.connect(self.updatePatientClick)
        self.ui.upReturnButton.clicked.connect(self.menuClick)

        self.ui.vpMenuButton.clicked.connect(self.vpMenuClick)
        self.ui.vpReturnButton.clicked.connect(self.menuClick)

        Inventory.createDatabase(self.cur)        
      
    def loginClick(self):

        if Inventory().userLogin(self.cur, self.name.text(), self.pw.text()):           
            self.greeting.setText(f'Welcome, {self.name.text()}')
            self.menuClick()
        else: self.warning.setText('Invalid username or password')

    def logOutClick(self):
        self.warning.setText('')
        self.name.setText('')
        self.pw.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
    
    def registerClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.registerPage)

    def userRegistered(self):
 
        Inventory().userRegister(self.cur, self.con, self.rName.text(), self.rUser.text(), self.rPw.text())
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
    
    def menuClick(self):
        self.amName.setText('')
        self.amPur.setText('')
        self.amExp.setText('')
        self.amQty.setText('')
        self.amCost.setText('')
        self.amWarning.setText('')

        self.mID.setText('')
        self.umName.setText('')
        self.umPur.setText('')
        self.umExp.setText('')
        self.umQty.setText('')
        self.umCost.setText('')
        self.umWarning.setText('')

        self.apName.setText('')
        self.apAge.setText('')
        self.apGender.setText('')
        self.apWeight.setText('')
        self.apStatus.setText('')
        self.apMed.setText('')
        self.apRem.setText('')
        self.apWarning.setText('')

        self.pID.setText('')
        self.upName.setText('')
        self.upAge.setText('')
        self.upGender.setText('')
        self.upWeight.setText('')
        self.upStatus.setText('')
        self.upMed.setText('')
        self.upRem.setText('')
        self.upWarning.setText('')
        self.ui.stackedWidget.setCurrentWidget(self.ui.menuPage)

    def amMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.addMedicinePage)

    def addMedicineClick(self):
        self.amWarning.setText(Medicine.addMedicine(self.cur, self.con, self.amName.text(),
        self.amPur.text(), self.amExp.text(), self.amQty.text(), self.amCost.text()))

    def umMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.updateMedicinePage)

    def updateMedicineClick(self):
        self.umWarning.setText(Medicine.updateMedicine(self.cur, self.con, self.mID.text(),
        self.umName.text(), self.umPur.text(), self.umExp.text(), self.umQty.text(), self.umCost.text()))

    def vmMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewMedicinePage)
        model = Medicine.currentMedicines(self.cur)
        self.ui.vmTableView.setModel(model)

    def apMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.addPatientPage)

    def addPatientClick(self):
        self.apWarning.setText(Patient.addPatient(self.cur, self.con, self.apName.text(), self.apAge.text(),
        self.apGender.text(), self.apWeight.text(), self.apStatus.text(), self.apMed.text(), self.apRem.text()))

    def upMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.updatePatientPage)

    def updatePatientClick(self):
        self.upWarning.setText(Patient.updatePatient(self.cur, self.con, self.pID.text(), self.upName.text(), self.upAge.text(),
        self.upGender.text(), self.upWeight.text(), self.upStatus.text(), self.upMed.text(), self.upRem.text()))

    def vpMenuClick(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.viewPatientPage)
        model = Patient.currentPatients(self.cur)
        self.ui.vpTableView.setModel(model)