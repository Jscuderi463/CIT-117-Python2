# Author: Joseph Scuderi
# Due Date: 2/23/2025
# Assignment: Password Validator

# 1.) Prompt the user for their First and Last name and store in a variable called sName

sName = input("Enter First and Last Name")

sValid = False
iPassLength = False
sStartsWithPass = False
sUpper = False
sLower = False
iDigit = False
sSpecial = False
sInitials = False



#2.) Code a Loop to keep asking for a password UNTIL a valid password is provided.
#.3) Prompt user for their desired password and store in sPassword variable.
def get_Password():
    while sValid == False:
        sPassword = input("Enter new Password")
        return sPassword


#.4) Extract initials from sName and store in sInitials variable
def get_Initials():
    sInitials = sName[0] + sName[sName.find(" ")+1]
    return sInitials


#5.) Check to make sure the password provided is between 8 and 12 characters.
def get_Length():
    iPassLength = get_Password()
    if iPassLength > 8 and iPassLength <= 12:
        print("Password must be between 8 and 12 characters")
    else:
        iPassLength = False

#6.) Check to make sure the provided password does not start with PASS or any variation of it.
def get_Pass():
    if sPassword.lower().startswith("pass"):
        print("Password can't start with Pass")
    else: sStartsWithPass = True

#7.) Check to make sure the provided password has at least 1 uppercase letter A-Z
def get_Upper():
    for char in sPassword:
        if char.isupper() == True:
            print(f" Password must contain one Uppercase Letter")

#8.) Check to make sure the provided password has at least 1 Lowercase letter A-Z
def get_Lower():
    for char in sPassword:
        if char.islower() == True:
            print(f" Password must contain one Lowercase Letter")

#9.) Check to make sure the password contains at least 1 number
def get_Digit():
    for char in sPassword:
        if char.isdigit() == True:
            print(f" Password must contain at least one number 0-9 ")

#10.) Check to make sure the password contains one of these special characters ! @ # $ % ^
def get_Special():
    for char in sPassword:
        if char in "!@#$%^" == True:
            print(f" Password must contain at least one of these special characters")

#11.) Check to make sure the password does not contain the users's initials
def get_CheckInitials():
    if sInitials.lower() in sPassword.lower():
        print("Password can't contain user initials")
    else:
        sInitials = True



def main():
    sUserName = sName
    sPassword = get_Password()
    sInitials = get_Initials()
    iLength = get_Length()
    sUpper = get_Upper()
    sLower = get_Lower()
    iDigit = get_Digit()
    sSpecial = get_Special()
    sInitials = get_CheckInitials()

    print(f"Name: {sName} , Initials{sInitials} , Password: {sPassword}")
main()