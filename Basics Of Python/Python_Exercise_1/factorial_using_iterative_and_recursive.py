import math

def factorial_iterative(n):
    """Iterative approach to calculate factorial."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Recursive approach to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def gamma_function(x):
    """Gamma function (using math.gamma for float values)."""
    return math.gamma(x)

def print_program_description():
    print("Welcome to the Factorial and Gamma Calculator Program!")
    print("This program calculates the factorial of a given non-negative integer.")
    print("For non-integer values, the Gamma function will be computed.")
    print("A factorial of a number 'n' (denoted as n!) is the product of all positive integers less than or equal to 'n'.")
    print("For example, factorial of 5 (5!) is 5 * 4 * 3 * 2 * 1 = 120.")
    print("For fractional numbers, we calculate the Gamma function instead of the factorial.")

def get_input():
    """Function to handle user input and validate it."""
    while True:
        try:
            user_input = input("Enter a number (integer or float) to calculate its factorial or Gamma function: ")
            num = float(user_input)  # Parse input as float to handle both integers and floats
            if num < 0:
                print("Error: Factorial and Gamma function are not defined for negative numbers. Please try again.")
                continue
            return num
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def main():
    # Explain the program's functionality
    print_program_description()

    # Get valid input from the user
    num = get_input()

    # Check if the input is an integer or float
    if num.is_integer():  # If the number is an integer
        num = int(num)  # Convert to int
        # Calculate factorial using both approaches
        iterative_result = factorial_iterative(num)
        recursive_result = factorial_recursive(num)
        
        # Display factorial results
        print(f"\nFactorial of {num} using iterative approach: {iterative_result}")
        print(f"Factorial of {num} using recursive approach: {recursive_result}")
    else:
        # Calculate Gamma function for non-integer (float) input
        gamma_result = gamma_function(num + 1)  # Gamma(x + 1) corresponds to x!
        
        # Display Gamma result
        print(f"\nGamma function of {num} is: {gamma_result}")

# Run the program
main()
