#this code helps a financial company to calculate the investment and bond of the user#

#investment calculator is used to calculate the return on investment#

#bond calculate is used to calculate the repayment on home loan#

#for investment, the user must choose either a simple or compound interest to know the return on investment#


import math

investment = "To calculate the amount of interest you'll earn on investment"
bond = "To calculate the amount you'll have to pay on home loan"

calculator = input("Choose either investment or bond calculator:").lower()

if calculator == "investment":
    money = float(input("Enter the amount of money you want to deposit:"))
    interest_rate = int(input("Enter the interest rate:"))
    num_years = int(input("Enter the number of years you plan to invest for:"))
    interest = input("Do you want simple or compound interest?:")
    if interest == "simple":
        total_simple = (money) * (1 + (interest_rate) / 100 * (num_years))
        print(round(total_simple, 2))
    elif interest == "compound":
            total_compound = (money) * math.pow((1 + (interest_rate) / 100), (num_years))
            print(round(total_compound, 2))

#the return on investment for 20 years at 8% interest rate for compound interest is greater than the return on investment for simple interest#

if calculator == "bond":
    house_value = float(input("Please enter the present house value:"))
    interest_ratehouse = int(input("Please enter the interest rate:"))
    interest_ratehouse = interest_ratehouse / 100
    num_months = int(input("Enter the number of months to repay the bond:"))
    total = (float(interest_ratehouse / 12) * house_value) / (1 - (1 + interest_ratehouse / 12) ** -num_months)
    print(round(total, 2))

