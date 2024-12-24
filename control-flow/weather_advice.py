#Using Conditional statements to control the flow of execution in my program based on useer input regarding weather conditions

#Prompt user for input
condition = ["sunny", "rainy", "cold"]
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

#Provide recommendations based on input, using conditional statements
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")