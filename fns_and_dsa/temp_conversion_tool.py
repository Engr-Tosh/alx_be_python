#A script to convert temperatures via the illustration of variable scopes

#Store the conversion formulas appropriately 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = float(input("Enter the temperature to convert: "))
temp_unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
    

#Define the function to carry out the conversion operation
def convert_to_celsius(fahrenheit):     #formula to convert from fahrenheit to celsius is (F - 32) * 5/9
    return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius):     #formula to convert from celsius to fahrenheit is (C * 9/5) + 32
    return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#User interaction and control flow    

if 'F' == temp_unit:
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
elif 'C' == temp_unit:
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")


