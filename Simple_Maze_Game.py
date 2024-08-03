import random

def create_maze(width, height):
    maze = [['#'] * width for _ in range(height)]
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if x % 2 == 1 and y % 2 == 1:
                maze[y][x] = ' '
                if x < width - 2:
                    if random.choice([True, False]):
                        maze[y][x + 1] = ' '
                    else:
                        maze[y + 1][x] = ' '
    maze[1][1] = 'P'  # Player start
    maze[height - 2][width - 2] = 'G'  # Goal
    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(row))

def find_player(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'P':
                return x, y

def move_player(maze, direction):
    x, y = find_player(maze)
    if direction == 'up' and maze[y - 1][x] in ' G':
        maze[y][x], maze[y - 1][x] = ' ', 'P'
    elif direction == 'down' and maze[y + 1][x] in ' G':
        maze[y][x], maze[y + 1][x] = ' ', 'P'
    elif direction == 'left' and maze[y][x - 1] in ' G':
        maze[y][x], maze[y][x - 1] = ' ', 'P'
    elif direction == 'right' and maze[y][x + 1] in ' G':
        maze[y][x], maze[y][x + 1] = ' ', 'P'

def play_maze_game():
    width, height = 21, 21
    maze = create_maze(width, height)

    print("Welcome to the Maze Game!")
    print("Use 'w', 'a', 's', 'd' to move up, left, down, and right.")
    print("Reach 'G' to win the game.\n")

    while True:
        display_maze(maze)
        move = input("Move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            directions = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
            move_player(maze, directions[move])
            if maze[height - 2][width - 2] == 'P':
                display_maze(maze)
                print("Congratulations! You've reached the goal!")
                break

if __name__ == "__main__":
    play_maze_game()
