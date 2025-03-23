import random

def number_guessing_game():
    # Step 1: Set the range for the number
    lower_bound = 1
    upper_bound = 100
    
    # Step 2: The computer randomly selects a number
    number_to_guess = random.randint(lower_bound, upper_bound)
   
    attempts = 0
    
    # Step 4: Provide an introductory message
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
  
    while True:
      
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
       
        attempts += 1
        
      