import sqlite3

connection = sqlite3.connect("database/HospitalDB.db")

cursor = connection.cursor()

print("Database Connected Successfully")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments(

DepartmentID INTEGER PRIMARY KEY,

DepartmentName TEXT NOT NULL

)
""")
print("Departments Table Created")

# doctors table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS Doctors(

DoctorID INTEGER PRIMARY KEY,

DoctorName TEXT NOT NULL,

Experience INTEGER,

DepartmentID INTEGER,

FOREIGN KEY(DepartmentID)

REFERENCES Departments(DepartmentID)

)
""")

print("Doctors Table Created")
# patient table 

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients(

PatientID INTEGER PRIMARY KEY,

PatientName TEXT,

Age INTEGER,

Gender TEXT,

BMI REAL,

BloodPressure INTEGER,

Cholesterol INTEGER,

Glucose INTEGER,

Smoking TEXT,

Diabetes INTEGER,

DoctorID INTEGER,

FOREIGN KEY(DoctorID)

REFERENCES Doctors(DoctorID)

)
""")

print("Patients Table Created")

# appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Appointments(AppointmentID INTEGER PRIMARY KEY,
AppointmentDate TEXT,
Diagnosis TEXT,

PatientID INTEGER,
DoctorID INTEGER,
FOREIGN KEY(PatientID)  
REFERENCES Patients(PatientID),
FOREIGN KEY(DoctorID)
REFERENCES Doctors(DoctorID)

)
""")        
print("Appointments Table Created")

connection.commit()

connection.close()

print("Connection Closed")