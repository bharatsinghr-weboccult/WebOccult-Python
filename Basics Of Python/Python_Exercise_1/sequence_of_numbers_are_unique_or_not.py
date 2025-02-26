def all_unique():
    # Explanation of the program's purpose for the user
    print("This program will check if all the numbers in a sequence are unique.")
    print("You will be asked to enter a sequence of numbers separated by commas.")
    print("You can use spaces and commas in any combination, and they will be handled.")
    print("If all numbers are unique, it will say 'All numbers are unique.'")
    print("If there are any duplicates, it will say 'There are duplicate numbers.'")
    
    try:
        # Taking input from the user
        user_input = input("Enter a sequence of numbers separated by commas: ")

        # Clean up the input by removing extra spaces and handling multiple commas
        # Split the input by commas, strip spaces, and remove any empty elements
        sequence = [int(x.strip()) for x in user_input.split(',') if x.strip()]

        # Check if all numbers are unique
        if len(sequence) == len(set(sequence)):
            print("All numbers are unique.")
        else:
            print("There are duplicate numbers.")
    
    except ValueError:
        print("Invalid input! Please enter a sequence of numbers separated by commas.")

# Example usage:
all_unique()
