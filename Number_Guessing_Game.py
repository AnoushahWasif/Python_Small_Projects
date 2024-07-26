import random

def guess_number_game():
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0
    guessed = False

    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                guessed = True
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number_game()
