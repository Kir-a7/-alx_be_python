from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return (current_date)

def calculate_future_date(current_date):
    number_of_days= int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days) + current_date
    return future_date



valu = display_current_datetime()
future_date = calculate_future_date(current_date = valu)

print(f"Current date and time: {valu}")
print(f"Future date: {future_date}")