from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Extracting year, month, date, and time using lambda
year = lambda dt: dt.year
month = lambda dt: dt.month
day = lambda dt: dt.day
time = lambda dt: dt.time()

# Example usage
print(current_datetime)
print(year(current_datetime))
print(month(current_datetime))
print(day(current_datetime))
print(time(current_datetime))
