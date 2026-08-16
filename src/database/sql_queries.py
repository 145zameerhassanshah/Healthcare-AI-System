from pathlib import Path
import sqlite3
import pandas as pd

project_root = Path(__file__).resolve().parent.parent

database_path = project_root/"database"/"HospitalDB.db"

connection = sqlite3.connect(database_path)

print(pd.read_sql("SELECT * FROM Departments",connection))

print(pd.read_sql("SELECT * FROM Doctors LIMIT 10",connection))

print(pd.read_sql("SELECT * FROM Patients LIMIT 10",connection))

print(pd.read_sql("SELECT * FROM Appointments LIMIT 10",connection))

print(pd.read_sql("""

SELECT PatientName,Age,BMI

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT *

FROM Patients

WHERE Diabetes=1

""",connection))

print(pd.read_sql("""

SELECT *

FROM Patients

WHERE Age>50

AND BMI>25

""",connection))

print(pd.read_sql("""

SELECT *

FROM Patients

ORDER BY Glucose DESC

""",connection))

print(pd.read_sql("""

SELECT *

FROM Patients

LIMIT 20

""",connection))

print(pd.read_sql("""

SELECT DISTINCT Gender

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT COUNT(*) AS TotalPatients

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT AVG(BMI) AS AverageBMI

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT MAX(Glucose) AS HighestGlucose

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT MIN(Age) AS YoungestPatient

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT SUM(Diabetes) AS DiabetesPatients

FROM Patients

""",connection))

print(pd.read_sql("""

SELECT Gender,

COUNT(*) AS Total

FROM Patients

GROUP BY Gender

""",connection))

print(pd.read_sql("""

SELECT Gender,

COUNT(*) AS Total

FROM Patients

GROUP BY Gender

HAVING COUNT(*)>100

""",connection))

print(pd.read_sql("""

SELECT

P.PatientName,

D.DoctorName,

Dep.DepartmentName

FROM Patients P

INNER JOIN Doctors D

ON P.DoctorID=D.DoctorID

INNER JOIN Departments Dep

ON D.DepartmentID=Dep.DepartmentID

LIMIT 20

""",connection))

print(pd.read_sql("""

SELECT

P.PatientName,

D.DoctorName,

A.AppointmentDate,

A.Diagnosis

FROM Appointments A

INNER JOIN Patients P

ON A.PatientID=P.PatientID

INNER JOIN Doctors D

ON A.DoctorID=D.DoctorID

LIMIT 20

""",connection))
18. GROUP BY Department
print(pd.read_sql("""

SELECT

Dep.DepartmentName,

COUNT(*) AS TotalDoctors

FROM Doctors D

INNER JOIN Departments Dep

ON D.DepartmentID=Dep.DepartmentID

GROUP BY Dep.DepartmentName

""",connection))

print(pd.read_sql("""

SELECT

Gender,

AVG(Glucose) AS AvgGlucose

FROM Patients

GROUP BY Gender

""",connection))

print(pd.read_sql("""

SELECT

PatientName,

Glucose

FROM Patients

ORDER BY Glucose DESC

LIMIT 10

""",connection))

print(pd.read_sql("""

SELECT

DoctorName,

Experience

FROM Doctors

ORDER BY Experience DESC

LIMIT 10

""",connection))

print(pd.read_sql("""

SELECT *

FROM Patients

WHERE Glucose>(

SELECT AVG(Glucose)

FROM Patients

)

""",connection))

print(pd.read_sql("""

SELECT

D.DoctorName,

COUNT(A.AppointmentID) AS TotalAppointments

FROM Doctors D

LEFT JOIN Appointments A

ON D.DoctorID=A.DoctorID

GROUP BY D.DoctorID

ORDER BY TotalAppointments DESC

""",connection))

print(pd.read_sql("""

SELECT

Diabetes,

COUNT(*) AS Total

FROM Patients

GROUP BY Diabetes

""",connection))

connection.close()

print("SQL Practice Completed Successfully")