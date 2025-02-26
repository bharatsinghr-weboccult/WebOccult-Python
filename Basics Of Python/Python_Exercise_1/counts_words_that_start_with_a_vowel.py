import re

def words_starting_with_vowel(word_list):
    # Print an explanation of what the program does    
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    
    # Create a new list to store words that start with a vowel
    result = []
    
    # Use regular expression to split the string by punctuation, but keep words like "apple's"
    for sentence in word_list:
        words = re.findall(r'\b\w+\'?\w*\b', sentence)  # Match words including apostrophes
        for word in words:
            if word[0] in vowels:  # Check if the word starts with a vowel
                result.append(word)
    
    return result

print("This program filters sentence and returns all words that start with a vowel (a, e, i, o, u).")
sentences = [input("enter your sentence : ")]
result = words_starting_with_vowel(sentences)
print("\nWords that start with a vowel:", result)
