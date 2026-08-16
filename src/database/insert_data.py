from pathlib import Path
import sqlite3
import random

# -----------------------------
# Database Connection
# -----------------------------

project_root = Path(__file__).resolve().parent.parent
database_path = project_root / "database" / "HospitalDB.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

print("Database Connected Successfully")

# ===========================================================
# INSERT DEPARTMENTS
# ===========================================================

departments = [

(1,"Cardiology"),
(2,"Neurology"),
(3,"Orthopedics"),
(4,"General Medicine"),
(5,"Pediatrics"),
(6,"Dermatology"),
(7,"Oncology"),
(8,"ENT"),
(9,"Psychiatry"),
(10,"Emergency")

]

cursor.execute("DELETE FROM Departments")

cursor.executemany("""

INSERT INTO Departments
(DepartmentID,DepartmentName)

VALUES (?,?)

""",departments)

print("Departments Inserted Successfully")

# ===========================================================
# INSERT DOCTORS
# ===========================================================

doctor_names = [

"Dr Ali",
"Dr Ahmed",
"Dr Hassan",
"Dr Fatima",
"Dr Sana",
"Dr Bilal",
"Dr Ayesha",
"Dr Hamza",
"Dr Usman",
"Dr Maryam",
"Dr Abdullah",
"Dr Zain",
"Dr Hina",
"Dr Saad",
"Dr Umer",
"Dr Amna",
"Dr Ibrahim",
"Dr Noor",
"Dr Salman",
"Dr Mahnoor"

]

cursor.execute("DELETE FROM Doctors")

doctors=[]

for doctor_id in range(1,51):

    doctor=(

        doctor_id,

        random.choice(doctor_names),

        random.randint(2,25),

        random.randint(1,10)

    )

    doctors.append(doctor)

cursor.executemany("""

INSERT INTO Doctors

(DoctorID,DoctorName,Experience,DepartmentID)

VALUES (?,?,?,?)

""",doctors)

print("Doctors Inserted Successfully")

# ===========================================================
# INSERT PATIENTS
# ===========================================================

first_names = [
    "Ali","Ahmed","Hassan","Fatima","Ayesha","Bilal","Hamza",
    "Usman","Sana","Maryam","Saad","Umer","Noor","Mahnoor",
    "Abdullah","Ibrahim","Hina","Zain","Salman","Amna"
]

genders = ["Male","Female"]
smoking = ["Yes","No"]

cursor.execute("DELETE FROM Patients")

patients=[]

for patient_id in range(1,1001):

    age=random.randint(18,80)

    bmi=round(random.uniform(18.0,35.0),1)

    bp=random.randint(90,180)

    cholesterol=random.randint(120,320)

    glucose=random.randint(70,240)

    smoke=random.choice(smoking)

    diabetes=1 if glucose>140 else 0

    patient=(

        patient_id,

        random.choice(first_names)+" "+str(patient_id),

        age,

        random.choice(genders),

        bmi,

        bp,

        cholesterol,

        glucose,

        smoke,

        diabetes,

        random.randint(1,50)

    )

    patients.append(patient)

cursor.executemany("""

INSERT INTO Patients

(PatientID,PatientName,Age,Gender,BMI,BloodPressure,Cholesterol,Glucose,Smoking,Diabetes,DoctorID)

VALUES (?,?,?,?,?,?,?,?,?,?,?)

""",patients)

print("1000 Patients Inserted Successfully")

# ===========================================================
# INSERT APPOINTMENTS
# ===========================================================

diagnosis = [
"Diabetes",
"Hypertension",
"Flu",
"Fever",
"Asthma",
"Heart Disease",
"Migraine",
"Fracture",
"Skin Allergy",
"Routine Checkup"
]

cursor.execute("DELETE FROM Appointments")

appointments=[]

for appointment_id in range(1,3001):

    patient_id=random.randint(1,1000)

    doctor_id=random.randint(1,50)

    month=random.randint(1,12)

    day=random.randint(1,28)

    AppointmentDate=f"2026-{month:02d}-{day:02d}"

    appointment=(

        appointment_id,

        patient_id,

        doctor_id,

        AppointmentDate,

        random.choice(diagnosis)

    )

    appointments.append(appointment)

cursor.executemany("""

INSERT INTO Appointments

(AppointmentID,PatientID,DoctorID,AppointmentDate,Diagnosis)

VALUES (?,?,?,?,?)

""",appointments)

print("3000 Appointments Inserted Successfully")

# ===========================================================
# SAVE & CLOSE
# ===========================================================

connection.commit()

print("Database Saved Successfully")

connection.close()

print("Connection Closed Successfully")