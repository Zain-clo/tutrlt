import random

def number_guessing_game():
    # Step 1: Set the range for the number
    lower_bound = 1
    upper_bound = 100
    
    # Step 2: The computer randomly selects a number
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    # Step 3: Set the initial number of attempts
    attempts = 0
    
    # Step 4: Provide an introductory message
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    # Step 5: Start the game loop
    while True:
        # Step 6: Ask the player for a guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        # Step 7: Increase the number of attempts
        attempts += 1
        
        # Step 8: Check if the guess is correct, too
