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
            # Define the symbols you want to split by
            delimiters = ['*', '-', '+', '/', ' ']

            # Initialize an empty list to store the result
            result = []

            # Initialize a temporary string to build words
            temp = ""

            # Loop through each character in the text
            for char in user_input:
                if char in delimiters:
                    if temp:
                        result.append(temp)  # Add the word to the result
                        temp = ""  # Reset the temporary string
                    if char != ' ':
                        result.append(char)  # Add the delimiter to the result (excluding space)
                else:
                    temp += char  # Build the word
            # Add the last number if there's any
            if temp:
                result.append(temp)
                
            # Ensure input has exactly 3 result: number operator number
            if len(result) != 3:
                raise FormulaError("Formula must have exactly 3 elements: number operator number.")
            
            # Attempt to convert the first and third elements to float
            num1 = float(result[0])
            num2 = float(result[2])
            
            # Validate operator
            operator = result[1]
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
