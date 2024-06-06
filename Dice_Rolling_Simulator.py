import random

def roll_dice():

    dice_drawing = {
        1: (
            "---------",
            "|       |",
            "|   O   |",
            "|       |",
            "---------"
        ),
        2: (
            "---------",
            "| O     |",
            "|       |",
            "|     O |",
            "---------"
        ),
        3: (
            "---------",
            "| O     |",
            "|   O   |",
            "|     O |",
            "---------"
        ),
        4: (
            "---------",
            "| O   O |",
            "|       |",
            "| O   O |",
            "---------"
        ),
        5: (
            "---------",
            "| O   O |",
            "|   O   |",
            "| O   O |",
            "---------"
        ),
        6: (
            "---------",
            "| O   O |",
            "| O   O |",
            "| O   O |",
            "---------"
        )
    }
    roll = input("Do you want to roll the dice? (yes/no): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("You rolled: " + str(dice1) + " and " + str(dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Do you want to roll the dice again? (yes/no): ")

roll_dice()