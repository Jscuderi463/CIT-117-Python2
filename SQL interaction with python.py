# Author: Joseph Scuderi
# Due Date: 5/11/2025
# Sql Interaction Assignment

import sqlite3

dbConnection = sqlite3.connect("myDatabase.db")
dbCursor = dbConnection.cursor()

try:
    sCreateTable = "Create Table Employee(EmployeeID int, Name text)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    sCreateTable = "Create Table Pay(EmployeeID int, year int, Earnings real)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    sCreateTable = "Create Table SocialSecurity(Year int, Minimun real)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    bdConnection.commit()

except sqlite3.OperationError: print("Could Not create table")



sInsertPay = "Insert INTO Pay (EmployeeID, year, Earnings) Values("
sInsertPayReset = sInsertPay

with open("Pay.txt", "r") as file:
    iRows =0

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        sInsertPay += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertPay)

        try:
            dbConnection.execute(sInsertPay)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")
        sInsertPay = sInsertPayReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")


sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee
with open("Employee.txt", "r") as file:
    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        sInsertEmployee += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertEmployee)

        try:
            dbConnection.execute(sInsertEmployee)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")
        sInsertEmployee = sInsertEmployeeReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")



sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurity(Year, Minimum) VALUES("
sInsertSocialSecurityMinimumRest = sInsertSocialSecurityMinimum
with open("SocialSecurity.txt", "r") as file:
    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        sInsertSocialSecurityMinimum += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertSocialSecurityMinimum)

        try:
            dbConnection.execute(sInsertSocialSecurityMinimum)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")
        sInsertSocialSecurityMinimum = sInsertSocialSecurityMinimumRest

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")



dbCursor.execute("""
    SELECT a.Name, b.year, c.Earnings, d.Minimum
    FROM Employee AS a
    JOIN Pay AS b
    JOIN SocialSecurityMinimum AS d
    ON d.year = b.year;
    """)


print(f"{'Employee Name':<20} {'Year':<5} {'Earnings':>15} {'Min':>15}{'Include':>15}")
for row in dbCursor.fetchall():

    fResult = ""

    if row[2] >= row[-1]: fResult ="yes"

    else: fResult = "NO"

    print(f"{row[0]:<20} {row[1]:<5} {row[2]:>15,.2f} {row[3]:>15,.2f}{fResult:>15}")
