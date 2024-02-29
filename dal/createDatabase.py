def createDatabase(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS Medicines(
                Medicine_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Medicine_Name varchar(100),
                Medicine_Purpose varchar(100),
                Medicine_Expiry varchar(100),
                Medicine_Quantity INTEGER,
                Medicine_Cost INTEGER
                );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Patients(
                Patient_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Patient_Name varchar(100),
                Patient_Age INTEGER ,
                Patient_Gender varchar(100),
                Patient_Weight INTEGER ,
                Patient_Status varchar(100),
                Patient_Medicine varchar(100),
                Patient_Remarks varchar(100)
                );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS User_Info(
                User_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                User_Name string,
                User_Email string,
                User_Password string
                );""")