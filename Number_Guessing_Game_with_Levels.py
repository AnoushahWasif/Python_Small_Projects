import random

def play_game(level):
    if level == 1:
        max_num = 10
        attempts = 5
    elif level == 2:
        max_num = 50
        attempts = 7
    elif level == 3:
        max_num = 100
        attempts = 10
    else:
        print("Invalid level")
        return

    number = random.randint(1, max_num)
    print(f"Guess the number between 1 and {max_num}. You have {attempts} attempts.")

    for _ in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return

    print(f"Sorry, you've used all your attempts. The number was {number}.")

def main():
    print("Welcome to the Number Guessing Game!")
    print("Choose a level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    level = int(input("Enter level (1, 2, or 3): "))

    play_game(level)

if __name__ == "__main__":
    main()
