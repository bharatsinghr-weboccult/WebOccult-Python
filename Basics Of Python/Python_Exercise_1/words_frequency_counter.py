import re
from collections import Counter

def count_word_frequency(text):
    # Regular expression to match words (ignores special characters except apostrophe)
    words = re.findall(r'\b[a-zA-Z0-9\'-]+\b', text.lower())  # case-insensitive and allows apostrophes
    # Use Counter to count word frequencies
    word_count = Counter(words)
    return word_count

# Take input from the user
text_input = input("Enter text to count word frequency: ")

# Display what the program does
print("\nProgram Explanation:")
print("This program takes the input text, splits it by any special character except apostrophe (').")
print("It counts the frequency of each word and displays the result in a dictionary format.")

# Call the function and display the result
word_frequencies = count_word_frequency(text_input)
print("\nWord Frequency Count:")
print(word_frequencies)
