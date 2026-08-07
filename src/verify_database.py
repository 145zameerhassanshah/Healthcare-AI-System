from pathlib import Path
import sqlite3
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

database_path = project_root/"database"/"HospitalDB.db"

connection=sqlite3.connect(database_path)

tables=["Departments","Doctors","Patients","Appointments"]

print("="*50)

print("DATABASE SUMMARY")

print("="*50)

for table in tables:

    query=f"SELECT COUNT(*) FROM {table}"

    count=pd.read_sql(query,connection)

    print(f"{table}: {count.iloc[0,0]} Records")

print("\nSample Patients")

print(pd.read_sql("SELECT * FROM Patients LIMIT 10",connection))

print("\nSample Doctors")

print(pd.read_sql("SELECT * FROM Doctors LIMIT 10",connection))

print("\nSample Appointments")

print(pd.read_sql("SELECT * FROM Appointments LIMIT 10",connection))

print("\nJOIN Verification")

query="""

SELECT

P.PatientName,

D.DoctorName,

Dep.DepartmentName,

A.AppointmentDate,

A.Diagnosis

FROM Appointments A

JOIN Patients P

ON A.PatientID=P.PatientID

JOIN Doctors D

ON A.DoctorID=D.DoctorID

JOIN Departments Dep

ON D.DepartmentID=Dep.DepartmentID

LIMIT 20

"""

print(pd.read_sql(query,connection))

connection.close()

print("\nDatabase Verification Completed Successfully")