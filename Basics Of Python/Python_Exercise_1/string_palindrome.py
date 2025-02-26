def is_palindrome(s):
    """
    Function to check whether a given string is a palindrome.
    Ignores spaces, punctuation, and capitalization.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

def print_program_description():
    print("\nWelcome to the Palindrome Checker Program!")
    print("This program checks whether the given string is a palindrome.")
    print("A palindrome is a word, phrase, or number that reads the same forward and backward.")
    print("The program will ignore spaces, punctuation, and capitalization when checking for a palindrome.")
    print('''\n\nFor example, the phrase "A man, a plan, a canal, Panama" is a palindrome \nbecause it reads the same forward and backward (ignoring spaces and punctuation).''')
    print("Let's check if your input is a palindrome!\n")

# Main function to run the program
def main():
    # Explain the program's functionality
    print_program_description()

    # Get user input
    input_string = input("Enter a string to check if it is a palindrome: ")

    # Check if the string is a palindrome
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

# Run the program
main()
