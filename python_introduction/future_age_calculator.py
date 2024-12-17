'''Practicing receiving user input withscript that asks the user for their current age 
And then calculates how old they will be in a specific future year
'''

future_years = 2050 - 2023
#prompt user to inout their age.
current_age = int(input("How old are you? "))

#calcaluting the future age
future_age = current_age + future_years

#output user's future age
print("In 2050, you will be", future_age, "years old.")