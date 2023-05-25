import math

# ask user choose between "investment" and "bond", making sure caplitalises doesn't influence validation
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
financial_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# validate user input
while financial_type != "investment" and financial_type != "bond":
    financial_type = input("Invalid input. Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

print(f"You choose {financial_type}")

# programme regarding "investment" type
if financial_type == "investment":
    deposit = float(input("Please enter the amount of money that you're depositing: "))

# use a while True loop to ensure getting valid input
# use a try-except block to catch invalid inputs
# use an else block to break if the input is valid
# idea comes from https://www.python-engineer.com/posts/ask-user-for-input/
    while True:
        try:
            interest_rate = float(input("Please enter the interest rate in %: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    investment_years = int(input("Please input the number of years you plan on investing: "))
    interest = input("Please choose either 'simple' or 'compound' interest that you prefer: ").lower()

# validate user input
    while interest != "simple" and interest != "compound":
        interest = input("Invalid input. Please choose either 'simple' or 'compound' interest that you prefer: ").lower()

# calculate final amount by using simple interest
    if interest == "simple":
        final_amount = round((deposit*(1+interest_rate/100*investment_years)), 2)
        print(f"You deposit {deposit}. Your interest rate is {interest_rate}%. You choose {interest} interest. After {investment_years} years, you will get {final_amount} in total!")

# calculate final amount by using compound interest
    else:
        final_amount = round((deposit * math.pow((1+interest_rate/100), investment_years)), 2)
        print(f"You deposit {deposit}. Your interest rate is {interest_rate}. You choose {interest} interest. After {investment_years} years, you will get {final_amount} in total!")

# programme regarding "bond" type
else:
    house_value = float(input("Please input the present value of the house: "))

# use a while True loop to ensure getting valid input
# use a try-except block to catch invalid inputs
# use an else block to break if the input is valid
# idea comes from https://www.python-engineer.com/posts/ask-user-for-input/
    while True:
        try:
            interest_rate = float(input("Please enter the interest rate in %: "))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    number_months = int(input("Please input the number of months you're planning to repay the bond: "))
    monthly_repay = round((interest_rate/100/12*house_value)/(1-(1+interest_rate/100/12)**(-number_months)), 2)
    print(f"The present value of the house is {house_value}. The interest rate is {interest_rate}%. \nIf you plan to repay the bond in {number_months} months, then you need to repay {monthly_repay} each month.")
