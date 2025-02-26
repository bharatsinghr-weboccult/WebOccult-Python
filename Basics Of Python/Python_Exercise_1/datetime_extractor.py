import re
from datetime import datetime

def print_program_description():
    print("Welcome to the Date and Time Extractor Program!")
    print("This program extracts the year, month, date, and time from a given datetime string.")
    print("For example, for the input '2020-01-15 09:03:32.744178', it will extract:")
    print("Year: 2020, Month: 01, Date: 15, Time: 09:03:32.744178")

def get_input():
    """Function to handle user input and validate it."""
    while True:
        try:
            # Get input from user
            user_input = input("Enter a datetime string (YYYY-MM-DD HH:MM:SS.ssssss): ")

            # Try to parse the input as a datetime string
            datetime_object = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S.%f")
            return user_input  # If input is valid, return the valid input
        except ValueError:
            print("Error: Invalid datetime format. Please enter the datetime in the format 'YYYY-MM-DD HH:MM:SS.ssssss'.")

def extract_date_time(input_string):
    """Lambda function to extract year, month, date, and time."""
    try:
        # Lambda function to extract parts
        extract = lambda date_time: {
            'year': date_time.year,
            'month': date_time.month,
            'day': date_time.day,
            'time': date_time.strftime("%H:%M:%S.%f")
        }
        
        # Convert input string to datetime object
        date_time_object = datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S.%f")
        
        # Extract using lambda function
        result = extract(date_time_object)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Display program description
    print_program_description()

    # Get valid datetime input from the user
    user_input = get_input()

    # Extract date and time components using Lambda function
    result = extract_date_time(user_input)

    # Display the extracted components
    if result:
        print(f"\nExtracted Information:")
        print(f"Year: {result['year']}")
        print(f"Month: {result['month']}")
        print(f"Day: {result['day']}")
        print(f"Time: {result['time']}")

# Run the program
main()
