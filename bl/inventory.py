from PyQt5.QtGui import QStandardItemModel, QStandardItem
from dal import DataAccess
from dal import createDatabase

#There should be a code in the DAL that creates Inventory objects using SQL

#for the purposes of login, there should be a list of names and list of passwords
listOfNames = ['admin','admin2']
listOfPasswords = ['pw','pw2']

class Inventory():
    def createDatabase(cur):
        createDatabase.createDatabase(cur)

    def userRegister(self, cur, con, name, email, password):
        DataAccess.registerUser(cur, con, name, email, password)

    def userLogin(self, cur, username, password):
        if DataAccess.validateUser(cur, username, password):
            return True
        else:
            return False

class Medicine():
    def addMedicine(cur, con, name, pur, exp, qty, cost):
        if(not name or not pur or not exp or not qty or not cost):
            return "Please fill all fields!"
        elif(not canBeInt(qty)):
            return "Quantity value must be an integer!"
        elif(not canBeInt(cost)):
            return "Cost value must be an integer!"
        else:
            DataAccess.addMedicine(cur, con, name, pur, exp, qty, cost)
            return "Medicine added!"
    
    def updateMedicine(cur, con, mID, name, pur, exp, qty, cost):        
        if(not mID or not name or not pur or not exp or not qty or not cost):
            return "Please fill all fields!"
        elif(not canBeInt(mID)):
            return "ID value must be an integer!"
        elif(not canBeInt(qty)):
            return "Quantity value must be an integer!"
        elif(not canBeInt(cost)):
            return "Cost value must be an integer!"
        elif(not DataAccess.isMedicineInDB(cur, mID)):
            return "Medicine ID not found!"        
        else:
            DataAccess.updateMedicine(cur, con, mID, name, pur, exp, qty, cost)
            return "Medicine updated!"
    
    def currentMedicines(cur):
            data = DataAccess.displayAllMedicines(cur)
            model = QStandardItemModel(len(data), len(data[0]))
            model.setHorizontalHeaderLabels(['ID', 'Name', 'Purpose', 'Expiry', 'Quantity', 'Cost'])
            for row_num, row_data in enumerate(data):
                for col_num, cell_data in enumerate(row_data):
                    cell = QStandardItem(str(cell_data))
                    model.setItem(row_num, col_num, cell)
            return model

class Patient():
    def addPatient(cur, con, name, age, gen, wei, sta, med, rem):
        if(not name or not age or not gen or not wei or not sta or not med or not rem):
            return "Please fill all fields!"
        elif(not canBeInt(age)):
            return "Age value must be an integer!"
        elif(not canBeInt(wei)):
            return "Weight value must be an integer!"
        else:
            DataAccess.addPatient(cur, con, name, age, gen, wei, sta, med, rem)
            return "Patient added!"
    
    def updatePatient(cur, con, pID, name, age, gen, wei, sta, med, rem):        
        if(not pID or not name or not age or not gen or not wei or not sta or not med or not rem):
            return "Please fill all fields!"
        elif(not canBeInt(pID)):
            return "ID value must be an integer!"
        elif(not canBeInt(age)):
            return "Age value must be an integer!"
        elif(not canBeInt(wei)):
            return "Weight value must be an integer!"
        elif(not DataAccess.isMedicineInDB(cur, pID)):
            return "Patient ID not found!"        
        else:
            DataAccess.updatePatient(cur, con, pID, name, age, gen, wei, sta, med, rem)
            return "Patient updated!"

    def currentPatients(cur):
        data = DataAccess.displayAllPatients(cur)
        model = QStandardItemModel(len(data), len(data[0]))
        model.setHorizontalHeaderLabels(['ID', 'Name', 'Age', 'Gender', 'Weight', 'Status', 'Medicine', 'Remarks'])
        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                cell = QStandardItem(str(cell_data))
                model.setItem(row_num, col_num, cell)
        return model

def canBeInt(s):
    try: (int(s))
    except ValueError:
        return False
    return True