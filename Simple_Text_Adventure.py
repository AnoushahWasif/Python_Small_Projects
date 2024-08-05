def show_instructions():
    print("Welcome to the Text Adventure Game!")
    print("Collect all items to win the game, or get eaten by the monster.")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'\n")

def show_status():
    print("---------------------------")
    print("You are in the " + current_room)
    print("Inventory: " + str(inventory))
    if "item" in rooms[current_room]:
        print("You see a " + rooms[current_room]["item"])
    print("---------------------------")

# Define the rooms and items
rooms = {
    'Hall': {'South': 'Kitchen', 'East': 'Dining Room', 'item': 'key'},
    'Kitchen': {'North': 'Hall', 'East': 'Garden', 'item': 'monster'},
    'Dining Room': {'West': 'Hall', 'South': 'Garden', 'item': 'potion'},
    'Garden': {'North': 'Dining Room', 'West': 'Kitchen', 'item': 'sword'}
}

# Initial game status
current_room = 'Hall'
inventory = []

# Show game instructions
show_instructions()

# Main game loop
while True:
    show_status()
    
    move = input(">").split()
    
    if move[0] == 'go':
        if move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print("You can't go that way!")
    elif move[0] == 'get':
        if "item" in rooms[current_room] and move[1] == rooms[current_room]['item']:
            inventory.append(move[1])
            print(move[1] + " got!")
            del rooms[current_room]['item']
        else:
            print("Can't get " + move[1] + "!")
    
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'monster':
        print("A monster has got you... GAME OVER!")
        break
    
    if len(inventory) == 3:
        print("You have collected all items and defeated the monster... YOU WIN!")
        break
