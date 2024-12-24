#Using for loop to generate and print a multiplication table 

#Prompt user for number which the multiplication table should be generated

number = int(input("Enter a number to see its multiplication table: "))

#generate multiplication table using for loops
for num in range(1, 11):
    product = number * num
    print(number, "*", num, "=", product)
    