# Description: A program for One Stop Insurance Company to enter and calculate new insurance policy information for it's customers.
# Author: Daniel Hayward
# Date: 2023-07-19

# Import required libraries
import datetime as DT
import validate as VA
import FormatValues as FV
from tqdm import tqdm
import time

# Main program
while True:

    # defining variables by reading from data file
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

    # Inputs for customer information
    custFirstName = input("Please enter the customer first name: ").title()
    custLastName = input("Please enter the customer last name: ").title()
    custAddress = input("Please enter the customer address: ")
    custCity = input("Please enter the customer city: ").title()

    # Province list for validation
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

    # Input and validate province input
    while True:
        custProvince = input("Please enter the customer province: ").upper()
        if custProvince == "":
            print("Error - Province cannot be blank.")
        elif custProvince not in validProv:
            print("Error - Invalid province entered.")
        else:
            break
    
    # Input more customer information
    custPostal = input("Please enter the customer postal code: ").upper()
    custPhone = input("Please enter the customer phone number: ")
    custCars = int(input("Please enter the number of cars being insured: "))
    
    # Input for optional services
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
    
    # List to validate payment method
    payMethodLST = [
        "Full",
        "Monthly"
    ]

    # Input the payment method
    while True:
        payMethod = input("Please enter whether it is paid in full or monthly (Full or Monthly): ").title()
        if payMethod == "":
            print("Error - Payment method cannot be blank.")
        elif payMethod not in payMethodLST:
            print("Error - Payment method may only be Full or Monthly.")
        else:
            break
    
    # Calculate the discount on the premium
    if custCars > 1:

        Discount = 0
        discountFull = 0
        for i in range(custCars - 1):
            Discount += basicPremium * addDiscount
            discountFull += basicPremium - Discount

    # Calulate the base premium for the policy
    Premiums = basicPremium + discountFull

    # Calculate extra costs
    totalExtra = 0

    if extraLiability == "Y":
        totalExtra += liabilityCost * custCars
    
    if optionalGlass == "Y":
        totalExtra += glassCost * custCars
    
    if optionalLoaner == "Y":
        totalExtra += loanerCost * custCars

    # Calulate totals
    totalPremium = Premiums + totalExtra

    taxCost = totalPremium * HSTRATE

    totalCost = totalPremium + taxCost

    monthlyPayment = (totalCost + 39.99) / 8

    # Get the invoice date and format it
    invoiceDate = DT.datetime.now()
    invoiceDateFormat = DT.datetime.strftime(invoiceDate, '%Y-%m-%d')

    # Calculate the next payment date for monthly payments
    nextPaymentDate = invoiceDate.replace(day = 1, month = invoiceDate.month + 1)
    
    # Output
    print("="*75)
    print("| One Stop Insurance Company")
    print("| Policy Information")
    print("="*75)
    print(f"| Customer Information: ")
    print("|")
    print(f"| Customer Name:          {custFirstName} {custLastName}")
    print(f"| Customer Address:       {custAddress} {custCity}, {custProvince}")
    print(f"| Customer Postal Code:   {custPostal}")
    print(f"| Customer Phone:         {custPhone}")
    print("="*75)
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
    print("="*75)
    print("| Extra Costs: ")
    print("|")
    if extraLiability == "Y":
        print(f"| Extra Liability Cost:   {FV.FDollar2(liabilityCost*custCars)}")
    if optionalGlass == "Y":
        print(f"| Optional Glass Cost:    {FV.FDollar2(glassCost*custCars)}")
    if optionalLoaner == "Y":
        print(f"| Optional Loaner Cost:   {FV.FDollar2(loanerCost*custCars)}")
    print("|")
    print(f"| Total Extra Cost:       {FV.FDollar2(totalExtra)}")
    print("="*75)
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
        print(f"| Next payment Date:      {nextPaymentDate}")
    print("="*75)
    print(f"Invoice date: {invoiceDateFormat}")
    print()

    # Write the invoice data to the Policies.dat file
    f = open("Policies.dat", "a")
    f.write(f"{str(policyNumber)}, {invoiceDateFormat}, {custFirstName}, {custLastName}, {custAddress}, {custCity}, {custProvince}, {custPostal}, {custPhone[0:3]}-{custPhone[3:6]}-{custPhone[6:11]}, {str(custCars)}, {extraLiability}, {optionalGlass}, {optionalLoaner}, {str(totalPremium)}\n")
    f.close()

    # Progress bar
    print("Saving invoice - please wait")
    for _ in tqdm(range(20), desc="Saving", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Data successfully saved ...")
    time.sleep(1)

    # Prompt the user to enter another policy
    while True:
        repeat = input("Did you want to process another invoice? (Y for yes, N for no): ").upper()
        if VA.validLetter(repeat, "Y", "N"):
            break

    if repeat == "Y":
        policyNumber += 1
        continue
    else:
        break







