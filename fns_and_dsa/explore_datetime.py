from datetime import datetime, timedelta 

now_date_time = datetime.now()

def display_current_datetime():
    current_date = now_date_time.date()
    print(current_date)

print(f"Current date and time: {now_date_time.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    future_date = now_date_time + timedelta(days=int(input("Enter the number of days to add to the current date: ")))
    print(f"Future date: {future_date.strftime("%y-%m-%d")}")

calculate_future_date()