#This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

'''
A quick understandable set instructions/steps:
Ask user for financial details
With that data calculate the montthly savings
Calculate the projected annual savings
Output savings
'''

#Prompt user for monthly income and monthly expense
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


#calculate the monthly savings 
monthly_savings = monthly_income - monthly_expenses
float(monthly_savings)

#Project annual savings (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * rate))
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
float(projected_savings)

print("Your monthly savings are $", monthly_savings,)
print("Projected savings after one year, with interest, is: $", projected_savings,)