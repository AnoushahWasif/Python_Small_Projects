import random

exit = False
user_score = 0
computer_score = 0

while exit == False:
    print("Welcome to Rock, Paper, Scissors!")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_choice = int(input("Enter your choice: "))
    computer_choice = random.randint(1, 3)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Computer wins! Paper beats Rock.")
            computer_score += 1
        else:
            print("You win! Rock beats Scissors.")
            user_score += 1
    elif user_choice == 2:
        if computer_choice == 1:
            print("You win! Paper beats Rock.")
            user_score += 1
        else:
            print("Computer wins! Scissors beats Paper.")
            computer_score += 1
    elif user_choice == 3:
        if computer_choice == 1:
            print("Computer wins! Rock beats Scissors.")
            computer_score += 1
        else:
            print("You win! Scissors beats Paper.")
            user_score += 1
    else:
        print("Invalid choice. Please try again.")

    print(f"User score: {user_score}")
    print(f"Computer score: {computer_score}")

    repeat = input("Would you like to play again? (Y/N): ")
    if repeat.lower() != "y":
        print("Program terminated")
        exit = True
    print("")
