#A script to set daily reminder based on user input task 

#prompt user for a single task
task = input("Enter your task?: ").lower()
priority = input("Priority level? (high/medium/low): ").lower()
time_bound = input("Is it time bound? (yes/no): ").lower()

print()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is a high priority task but it seems you should find the time for it though!")
    case "medium" | "low":
        print(f"Reminder: {task} is a {priority} task. Consider completing it when you have free time.")