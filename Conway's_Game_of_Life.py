import random
import time
import os

def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))

def get_neighbors(grid, row, col):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            count += grid[r][c]
    return count

def update_grid(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbors = get_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid

def play_game_of_life(rows, cols, generations):
    grid = create_grid(rows, cols)
    for _ in range(generations):
        display_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    play_game_of_life(20, 40, 100)
