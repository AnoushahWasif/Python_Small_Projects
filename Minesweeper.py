import random

def create_board(size, mines):
    board = [['0' for _ in range(size)] for _ in range(size)]
    mine_positions = set()

    while len(mine_positions) < mines:
        mine_positions.add((random.randint(0, size - 1), random.randint(0, size - 1)))

    for (r, c) in mine_positions:
        board[r][c] = 'M'

    for r in range(size):
        for c in range(size):
            if board[r][c] == 'M':
                continue
            mine_count = 0
            for i in range(max(0, r - 1), min(size, r + 2)):
                for j in range(max(0, c - 1), min(size, c + 2)):
                    if board[i][j] == 'M':
                        mine_count += 1
            board[r][c] = str(mine_count)

    return board

def print_board(board, revealed):
    size = len(board)
    for r in range(size):
        for c in range(size):
            if revealed[r][c]:
                print(board[r][c], end=' ')
            else:
                print('X', end=' ')
        print()

def reveal_cell(board, revealed, row, col):
    if board[row][col] == 'M':
        return False
    revealed[row][col] = True
    if board[row][col] == '0':
        size = len(board)
        for i in range(max(0, row - 1), min(size, row + 2)):
            for j in range(max(0, col - 1), min(size, col + 2)):
                if not revealed[i][j]:
                    reveal_cell(board, revealed, i, j)
    return True

def check_win(board, revealed):
    size = len(board)
    for r in range(size):
        for c in range(size):
            if board[r][c] != 'M' and not revealed[r][c]:
                return False
    return True

def play_minesweeper(size, mines):
    board = create_board(size, mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    print("Welcome to Minesweeper!")

    while True:
        print_board(board, revealed)
        row = int(input("Enter the row (0-{}): ".format(size - 1)))
        col = int(input("Enter the column (0-{}): ".format(size - 1)))

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Invalid input. Try again.")
            continue

        if not reveal_cell(board, revealed, row, col):
            print("Boom! You hit a mine. Game over.")
            break

        if check_win(board, revealed):
            print("Congratulations! You have cleared the board.")
            break

if __name__ == "__main__":
    play_minesweeper(5, 5)
