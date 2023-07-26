# Description: A program for One Stop Insurance Company to enter and calulcate new insurance policy information for it's customers.
# Author: Daniel Hayward
# Date: 2023-07-19

import datetime as DT
import validate as VA
import FormatValues as FV
from tqdm import tqdm
import time

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

    custFirstName = input("Please enter the customer first name: ").title()
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
        custProvince = input("Please enter the customer province: ").upper()
        if custProvince == "":
            print("Error - Province cannot be blank.")
        elif custProvince not in validProv:
            print("Error - Invalid province entered.")
        else:
            break
    
    custPostal = input("Please enter the customer postal code: ")
    custPhone = input("Please enter the customer phone number: ")
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
    
    if custCars > 1:

        Discount = 0
        discountFull = 0
        for i in range(custCars - 1):
            Discount += basicPremium * addDiscount
            discountFull += basicPremium - Discount

    
    Premiums = basicPremium + Discount

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

    invoiceDate = DT.datetime.now()
    invoiceDateFormat = DT.datetime.strftime(invoiceDate, '%Y-%m-%d')

    nextPaymentDate = invoiceDate.replace(day = 1, month = invoiceDate.month + 1)
    
    print("="*50)
    print("| One Stop Insurance Company")
    print("| Policy Information")
    print("="*50)
    print(f"| Customer Information: ")
    print("|")
    print(f"| Customer Name:          {custFirstName} {custLastName}")
    print(f"| Customer Address:       {custAddress} {custCity}, {custProvince}")
    print(f"| Customer Postal Code:   {custPostal}")
    print(f"| Customer Phone:         {custPhone}")
    print("="*50)
    print(f"| Policy Information: ")
    print("|")
    print(f"| Policy Number:          {policyNumber}")
    print(f"| Number of cars:         {custCars}")
    print(f"| Payment Method:         {payMethod}")
    if extraLiability == "Y":
        print("| Extra Liability: Yes")
    else:
        print("| Extra Liability: No")
    if optionalGlass == "Y":
        print("| Optionnal glass: Yes")
    else:
        print("| Optional glass: No")
    if optionalLoaner == "Y":
        print("| Optional Loaner Car: Yes")
    else:
        print("| Optional Loaner Car: No")
    print("="*50)
    print("| Extra Costs: ")
    print("|")
    if extraLiability == "Y":
        print(f"| Extra Liability Cost:   {FV.FDollar2(liabilityCost)}")
    if optionalGlass == "Y":
        print(f"| Optional Glass Cost:    {FV.FDollar2(glassCost)}")
    if optionalLoaner == "Y":
        print(f"| Optional Loaner Cost:   {FV.FDollar2(loanerCost)}")
    print("|")
    print(f"| Total Extra Cost:       {FV.FDollar2(totalExtra)}")
    print("="*50)
    print("| Policy Costs: ")
    print("|")
    print(f"| Basic Premium:          ${basicPremium}")
    print(f"| Discount:               {FV.FDollar2(Discount)}")
    print(f"| Total Premium:          ${totalPremium}")
    print(f"| Taxes:                  {FV.FDollar2(taxCost)}")
    print("|")
    print(f"| Total Cost:             {FV.FDollar2(totalCost)}")
    print("|")
    if payMethod == "Monthly":
        print(f"| Monthly Payment:        {FV.FDollar2(monthlyPayment)}")
    print("="*50)
    print(invoiceDateFormat)

    f = open("Policies.dat", "w")
    f.write(f"{str(policyNumber)}, ")
    f.write(f"{invoiceDate}, ")
    f.write(f"{custFirstName}, ")
    f.write(f"{custLastName}, ")
    f.write(f"{custAddress}, ")
    f.write(f"{custCity}, ")
    f.write(f"{custProvince}, ")
    f.write(f"{custPostal}, ")
    f.write(f"{custPhone[0:2]}-{custPhone[3:6]}-{custPhone[7:11]}, ")
    f.write(f"{str(custCars)}, ")
    f.write(f"{extraLiability}, ")
    f.write(f"{optionalGlass}, ")
    f.write(f"{optionalLoaner}, ")
    f.write(f"{payMethod}, ")
    f.write(f"{str(totalPremium)}\n ")
    f.close()

    print("Saving invoice - please wait")
    for _ in tqdm(range(20), desc="Saving", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Data successfully saved ...")
    time.sleep(1)

    while True:
        repeat = input("Did you want to process another invoice? (Y for yes, N for no): ").upper()
        if VA.validLetter(repeat, "Y", "N"):
            break

    if repeat == "Y":
        policyNumber += 1
        continue
    else:
        break







