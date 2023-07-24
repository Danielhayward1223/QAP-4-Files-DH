# Used to validate input values 
from datetime import datetime

def nameValid(Name):
    allowed_Char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-`")
    if Name == "":
        print("Error - name cannot be blank.")
    elif not set(Name).issubset(allowed_Char):
        print("Error - name must contain valid characters.")
    else:
        return True

def empNumValid(employeeNumber):
    allowed_Num = set("123456789")
    if employeeNumber == "":
        print("Error - Employee number cannot be blank.")
    elif not len(employeeNumber) == 5:
        print("Error - Employee number must be 5 digits.")
    elif not set(employeeNumber).issubset(allowed_Num):
        print("Error - Employee number must be 5 digits.")
    else:
        return True
    
def phoneValid(custPhone):
    if custPhone == "":
        print("Error - Phone number cannot be blank.")
    elif not len(custPhone) == 10:
        print("Error - Phone number must be 10 characters.")
    else:
        return True
    
def birthValid(empBirth):
    if empBirth == "":
        print("Error - Birth cannot be blank.")
    else:
        return True

def validLetter(Value, Letter1, Letter2):
    letterLST = [Letter1, Letter2]
    if Value == "":
        print("Error - Value must not be blank.")
    elif Value not in letterLST:
        print(f"Error - Invalid Entry must be an {Letter1} or {Letter2}")
    else:
        return True
    

def formatMoney(Value):
    formatted_Value = "{:,.2f}".format(Value)
    return formatted_Value