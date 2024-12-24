#Using for loop to generate and print a multiplication table 

#Prompt user for number which the multiplication table should be generated

number = int(input("Enter a number to see its multiplication table: "))
x = number
#generate multiplication table using for loops
for y in range(1, 11):
    product = float(x * y)
    z = product
    print(x, "*", y, "=", z)
    