import random

def initialize_board():
    return [['~'] * 5 for _ in range(5)]

def print_board(board):
    print("  0 1 2 3 4")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def place_ship(board):
    ship_row = random.randint(0, 4)
    ship_col = random.randint(0, 4)
    board[ship_row][ship_col] = 'S'
    return ship_row, ship_col

def get_user_guess():
    while True:
        try:
            row = int(input("Guess Row (0-4): "))
            col = int(input("Guess Col (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4:
                return row, col
            else:
                print("Invalid input. Enter numbers between 0 and 4.")
        except ValueError:
            print("Invalid input. Enter numbers between 0 and 4.")

def play_battleship():
    print("Welcome to Battleship!")
    board = initialize_board()
    ship_row, ship_col = place_ship(board)
    attempts = 5

    while attempts > 0:
        print_board(board)
        print(f"Attempts left: {attempts}")
        guess_row, guess_col = get_user_guess()

        if board[guess_row][guess_col] == 'S':
            print("Congratulations! You sunk my battleship!")
            break
        elif board[guess_row][guess_col] == 'X' or board[guess_row][guess_col] == 'O':
            print("You already guessed that spot.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = 'X'
            attempts -= 1

        if attempts == 0:
            print("Game Over! You ran out of attempts.")
            print(f"The battleship was at ({ship_row}, {ship_col}).")
            break

if __name__ == "__main__":
    play_battleship()
