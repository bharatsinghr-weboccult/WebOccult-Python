class FormulaError(Exception):
    """Custom exception for invalid formula input."""
    pass

def calculate():
    while True:
        # Prompt user for input
        user_input = input("Enter a formula (e.g., '1 + 1') or type 'quit' to exit: ")
        
        # Exit condition
        if user_input.lower() == "quit":
            print("Exiting the calculator.")
            break
        
        # Parse the input string
        try:
            parts = user_input.split()
            
            # Ensure input has exactly 3 parts: number operator number
            if len(parts) != 3:
                raise FormulaError("Formula must have exactly 3 elements: number operator number.")
            
            # Attempt to convert the first and third elements to float
            num1 = float(parts[0])
            num2 = float(parts[2])
            
            # Validate operator
            operator = parts[1]
            if operator not in ['+', '-', '*', '/']:
                raise FormulaError("Invalid operator. Only '+', '-', '*', and '/' are allowed.")
            
            # Perform calculation based on operator
            result = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}\
                .get(operator, "Invalid operator")
            
            # Print the result
            print(f"The result is: {result}")
        
        except FormulaError as fe:
            print(f"Error: {fe}")
        except ValueError:
            # This handles the case where float conversion fails
            print("Error: Invalid number format.")
            
# Run the calculator
calculate()
