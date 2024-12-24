#Using for loop to generate and print a multiplication table 

#Prompt user for number which the multiplication table should be generated

number = int(input("Enter a number to see its multiplication table: "))
X = number
#generate multiplication table using for loops
for Y in range(1, 11):
    product = float(X * Y)
    Z = product
    print(X,"*",Y,"=", Z)
    