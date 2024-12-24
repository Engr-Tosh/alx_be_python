#Utilizing while loops and nested for loops to draw a simple text based pattern

#Generate size from the user 
square_size = int(input("Enter the size of the pattern: "))
row = 0

while row < square_size:              #Outer while loop for number of rows 
    for col in range(1, square_size + 1):               #inner for loop for columns
        print("*", end="")
    print()                                #End current row
    row += 1                            #Go to next row (increment row by 1)
