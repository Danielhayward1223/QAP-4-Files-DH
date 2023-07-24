# Description: A program for One Stop Insurance Company to enter and calulcate new insurance policy information for it's customers.
# Author: Daniel Hayward
# Date: 2023-07-19

import datetime as dt
import validate as VA

def discountCalc(numCars):
    for i in range(numCars - 1):
        Discount = 869.00 * addDiscount
    return Discount

while True:

    f = open('OSICDef.dat', 'r')
    policyNumber = int(f.readline())
    basicPremium = float(f.readline())
    addDiscount = float(f.readline())
    liabilityCost = float(f.readline())
    glassCost = float(f.readline())
    loanerCost = float(f.readline())
    HSTRATE = float(f.readline())
    processFee = float(f.readline())
    f.close()

    custFirstName = input("Please enter the customer name: ").title()
    custLastName = input("Please enter the customer last name: ").title()
    custAddress = input("Please enter the customer address: ")
    custCity = input("Please enter the customer city: ").title()
    validProv = [
        'NL',
        'NB',
        'NS',
        'ON',
        'QB',
        'SK',
        'BC',
        'AB',
        'MN',
        'PEI',
    ]

    while True:
        custProvince = input("Please enter the customer province: ")
        if custProvince == "":
            print("Error - Province cannot be blank.")
        elif custProvince not in validProv:
            print("Error - Invalid province entered.")
        else:
            break
    
    custPostal = input("Please enter the customer postal code: ")
    custPhone = input("Please enter the customer phone number:")
    custCars = int(input("Please enter the number of cars being insured: "))
    
    while True:
        extraLiability = input("Please enter whether there is extra liability (Y for yes, N for no): ").upper()
        if VA.validLetter(extraLiability, 'Y', 'N'):
            break

    while True:
        optionalGlass = input("Please enter whether there is optional glass coverage (Y for yes, N for no): ").upper()
        if VA.validLetter(optionalGlass, 'Y', 'N'):
            break
    
    while True:
        optionalLoaner = input("Please enter whether they have an optional loaner car (Y for yes, N for no): ").upper()
        if VA.validLetter(optionalLoaner, 'Y', 'N'):
            break
    
    payMethodLST = [
        "Full",
        "Monthly"
    ]

    while True:
        payMethod = input("Please enter whether it is paid in full or monthly (Full or Monthly): ").title()
        if payMethod == "":
            print("Error - Payment method cannot be blank.")
        elif payMethod not in payMethodLST:
            print("Error - Payment method may only be Full or Monthly.")
        else:
            break
    
    Premiums = basicPremium + discountCalc(custCars)

    totalExtra = 0

    if extraLiability == "Y":
        totalExtra += liabilityCost
    
    if optionalGlass == "Y":
        totalExtra += glassCost
    
    if optionalLoaner == "Y":
        totalExtra += loanerCost

    totalPremium = Premiums + totalExtra

    taxCost = totalPremium * HSTRATE

    totalCost = totalPremium + taxCost

    monthlyPayment = (totalCost + 39.99) / 8

    invoiceDate = dt.datetime.now()
    dt.datetime.strftime(invoiceDate, '%Y-%m-%d')

    nextPaymentDate = invoiceDate.replace(day = 1, month = invoiceDate.month + 1)
    
    print("".ljust(50, "-"))
    print("{:<50}".format("One Stop Insurance Co."))
    print("{:<50}".format("Receipt"))
    print("".ljust(50, "-"))
    print("{:<22}{:<28}".format("Customer:", custFirstName + " " + custLastName))
    print("{:<22}{:<28}".format("Policy Number:", policyNumber))
    print("{:<22}{:<28}".format("Invoice Date:", invoiceDate))
    print("".ljust(50, "-"))
    print("{:<22}{:<28f}".format("Premiums:", basicPremium))
    print("{:<22}{:<28f}".format("Extra Liability:", liabilityCost if extraLiability == "Y" else 0))
    print("{:<22}{:<28f}".format("Optional Glass:", glassCost if optionalGlass == "Y" else 0))
    print("{:<22}{:<28f}".format("Optional Loaner:", loanerCost if optionalLoaner == "Y" else 0))
    print("".ljust(50, "-"))
    break

    