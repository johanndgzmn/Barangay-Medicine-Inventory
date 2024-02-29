def registerUser(cur, con, name, email, password):
    cur.execute('INSERT INTO User_Info(User_Name, User_Email, User_Password) VALUES (?, ?, ?)', (name, email, password))
    con.commit()


def validateUser(cur, email, password):
    cur.execute('SELECT User_Email, User_Password FROM User_Info WHERE User_Email = ? AND User_Password = ?', (email, password))
    result = cur.fetchone()
    
    if result is not None:
        return True
    else:
        return False
    
def displayAllUsers(cur):
    for row in cur.execute("SELECT * FROM User_Info"): print(row)

def addMedicine(cur, con, name, pur, exp, qty, cost):
    cur.execute("INSERT INTO Medicines VALUES (null, ?, ?, ?, ?, ?)",
                (name, pur, exp, qty, cost))
    con.commit()
    
def updateMedicine(cur, con, mID, name, pur, exp, qty, cost):
    cur.execute("""UPDATE Medicines
                SET Medicine_Name = ?,
                    Medicine_Purpose = ?,
                    Medicine_Expiry = ?,
                    Medicine_Quantity = ?,
                    Medicine_Cost = ?
                WHERE Medicine_ID = ?""", (name, pur, exp, qty, cost, mID))
    con.commit()

def displayAllMedicines(cur):
        cur.execute("SELECT * FROM Medicines")
        data = cur.fetchall()
        return data

def isMedicineInDB(cur, mID):
    cur.execute(f"SELECT 1 WHERE EXISTS(SELECT 1 FROM Medicines WHERE Medicine_ID = {mID})")
    found = cur.fetchone()
    if found: return(True)
    else: return(False)
    

def addPatient(cur, con, name, age, gen, wei, sta, med, rem):
    cur.execute("INSERT INTO Patients VALUES (null, ?, ?, ?, ?, ?, ?, ?)",
                (name, age, gen, wei, sta, med, rem))
    con.commit()
        
def updatePatient(cur, con, pID, name, age, gen, wei, sta, med, rem):
    print(pID, name, age, gen, wei, sta, med, rem)
    cur.execute(f"""UPDATE Patients
                SET Patient_Name = ?,
                    Patient_Age = ?,
                    Patient_Gender = ?,
                    Patient_Weight = ?,
                    Patient_Status = ?,
                    Patient_Medicine = ?,
                    Patient_Remarks = ?
                WHERE Patient_ID = ?""",
                (name, age, gen, wei, sta, med, rem, pID))
    con.commit()

def displayAllPatients(cur):
        cur.execute("SELECT * FROM Patients")
        data = cur.fetchall()
        return data