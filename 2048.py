import random
import curses

KEYS = {
    curses.KEY_UP: 'up',
    curses.KEY_DOWN: 'down',
    curses.KEY_LEFT: 'left',
    curses.KEY_RIGHT: 'right'
}

def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid

def add_random_tile(grid):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = 4 if random.random() < 0.1 else 2

def transpose(grid):
    return [list(row) for row in zip(*grid)]

def invert(grid):
    return [row[::-1] for row in grid]

def slide(row):
    new_row = [i for i in row if i != 0]
    while len(new_row) < 4:
        new_row.append(0)
    for i in range(3):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row

def move(grid, direction):
    if direction == 'left':
        return [slide(row) for row in grid]
    elif direction == 'right':
        return invert(move(invert(grid), 'left'))
    elif direction == 'up':
        return transpose(move(transpose(grid), 'left'))
    elif direction == 'down':
        return transpose(move(transpose(grid), 'right'))

def is_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
    for row in grid:
        for c in range(3):
            if row[c] == row[c + 1]:
                return False
    for c in range(4):
        for r in range(3):
            if grid[r][c] == grid[r + 1][c]:
                return False
    return True

def draw_grid(grid, screen):
    screen.clear()
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                screen.addstr(r * 2, c * 6, '.')
            else:
                screen.addstr(r * 2, c * 6, str(grid[r][c]))
    screen.refresh()

def main(screen):
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(100)

    grid = initialize_grid()
    draw_grid(grid, screen)

    while True:
        key = screen.getch()
        if key in KEYS:
            new_grid = move(grid, KEYS[key])
            if new_grid != grid:
                grid = new_grid
                add_random_tile(grid)
                draw_grid(grid, screen)
                if is_game_over(grid):
                    screen.addstr(10, 0, "Game Over!")
                    screen.refresh()
                    screen.getch()
                    break

if __name__ == "__main__":
    curses.wrapper(main)
