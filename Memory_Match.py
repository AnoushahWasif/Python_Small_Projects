import random
import os
import time

# Initialize the board
def initialize_board():
    board = list("AABBCCDDEEFFGGHH")
    random.shuffle(board)
    return [board[:4], board[4:8], board[8:12], board[12:]]

# Display the board
def display_board(board, mask):
    for i in range(4):
        for j in range(4):
            if mask[i][j]:
                print(board[i][j], end=' ')
            else:
                print('*', end=' ')
        print()

# Check if all pairs are matched
def check_win(mask):
    for row in mask:
        if not all(row):
            return False
    return True

# Play the game
def play_game():
    board = initialize_board()
    mask = [[False]*4 for _ in range(4)]

    print("Welcome to the Memory Match Game!")
    time.sleep(2)

    while not check_win(mask):
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board, mask)

        # Get the first choice
        print("\nEnter the coordinates of the first card (e.g., 0 1): ")
        x1, y1 = map(int, input().split())
        mask[x1][y1] = True
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board, mask)

        # Get the second choice
        print("\nEnter the coordinates of the second card (e.g., 1 2): ")
        x2, y2 = map(int, input().split())
        mask[x2][y2] = True
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(board, mask)

        if board[x1][y1] != board[x2][y2]:
            print("\nNo match!")
            mask[x1][y1] = False
            mask[x2][y2] = False
            time.sleep(2)
        else:
            print("\nIt's a match!")
            time.sleep(1)

    print("\nCongratulations! You matched all pairs!")

if __name__ == "__main__":
    play_game()
