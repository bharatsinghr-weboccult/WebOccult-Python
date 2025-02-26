import re

def count_students_above_90(grades_dict):
    """Count students with grades above 90."""
    count = sum(1 for grade in grades_dict.values() if grade > 90)
    return count

def get_grade_input():
    """Function to handle the input of grades."""
    while True:
        try:
            # Accepting grade input as float
            grade = float(input("Enter the grade (0-100): "))
            
            # Check if grade is valid (between 0 and 100)
            if grade < 0 or grade > 100:
                print("Error: Grade must be between 0 and 100. Please try again.")
                continue
            return grade
        except ValueError:
            # Handle invalid input (non-numeric)
            print("Error: Invalid input. Please enter a valid numeric grade (e.g., 95.5).")

def print_program_description():
    """Provide an explanation of the program."""
    print("Welcome to the Student Grade Program!")
    print("This program allows you to input student names and their grades.")
    print("It will then count how many students have grades above 90.")
    print("You will be prompted to enter the number of students you want to input.")
    print("After that, you will enter the names and grades for each student.\n")
    
def get_number_of_students():
    """Get valid input for the number of students."""
    while True:
        try:
            num_students = int(input("Enter the number of students you want to input: "))
            if num_students < 1:
                print("Error: The number of students must be at least 1. Please try again.")
                continue
            return num_students
        except ValueError:
            print("Error: Please enter a valid integer for the number of students.")

def get_student_name():
    """Get a valid student name (only alphabetic characters and spaces)."""
    while True:
        name = input("Enter the student's name: ").strip()
        
        # Check if name contains only alphabetic characters or spaces
        if not name or not re.match("^[A-Za-z ]+$", name):
            print("Error: Name must only contain alphabetic characters and spaces. Please try again.")
            continue
        return name

def main():
    # Explain the program's functionality
    print_program_description()

    # Get the number of students
    num_students = get_number_of_students()

    # Create an empty dictionary for student names and grades
    students_grades = {}

    # Accept student names and their grades
    for i in range(num_students):
        # Get valid student name
        name = get_student_name()

        # Get student grade
        grade = get_grade_input()

        # Store in the dictionary
        students_grades[name] = grade

    # Print the student grades dictionary
    print("\nStudent Grades Dictionary:", students_grades)
    
    # Call the function to count students with grades above 90
    count = count_students_above_90(students_grades)
    
    # Print the result
    print(f"\nNumber of students with grades above 90: {count}")

# Run the program
main()
