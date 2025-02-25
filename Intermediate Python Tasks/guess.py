import random

# Custom exception for invalid input
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function to get the user's guess
def get_user_guess(score):
    try:
        user_input = int(input(f"You have {score} attempt left\nGuess the secret number between 1 and 10: "))
        
        # Check if the number is in the valid range
        if user_input < 1 or user_input > 10:
            raise InvalidInputError("Please enter a valid integer between 1 and 10.")
        
        return user_input
    
    except ValueError:
        raise InvalidInputError("Invalid input. Please enter an integer.")
    except InvalidInputError as e:
        print(e)
        return None

# Main game loop
def play_game():
    print("Welcome to the Guessing Game!")
    while True:
        secret_number = random.randint(1, 10)
        guesses = 0
        score = 5
        
        print("I have selected a secret number between 1 and 10.")
        
        # Game loop until the correct guess
        while True:
            user_guess = None
            
            # Validate the guess
            while user_guess is None:
                user_guess = get_user_guess(score)
                
            
            score -= 1  # Score is higher for fewer guesses
            if user_guess == secret_number:
                print(f"Congratulations! You've guessed the correct number {secret_number}!")
                print(f"Your score: {score}")
                break
            elif not score:
                print(f"Your score: {score}")
                break
            elif user_guess < secret_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
