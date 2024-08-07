def show_instructions():
    print("""
Welcome to the Adventure Game!
==============================
Commands:
  go [direction] - Move in the specified direction (north, south, east, west)
  get [item] - Pick up an item
  inventory - Show your inventory
  help - Show the instructions
  quit - Exit the game
==============================
""")

def show_status(location, inventory, rooms):
    print(f"\nYou are in the {location}")
    print("Inventory:", inventory)
    if "item" in rooms[location]:
        print("You see a", rooms[location]["item"])

def play_game():
    rooms = {
        "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
        "Kitchen": {"north": "Hall", "item": "monster"},
        "Dining Room": {"west": "Hall", "south": "Garden", "item": "potion"},
        "Garden": {"north": "Dining Room"},
    }

    inventory = []
    location = "Hall"

    show_instructions()
    show_status(location, inventory, rooms)

    while True:
        move = input("\n>").lower().split()

        if move[0] == "go":
            if move[1] in rooms[location]:
                location = rooms[location][move[1]]
                show_status(location, inventory, rooms)
            else:
                print("You can't go that way!")

        elif move[0] == "get":
            if "item" in rooms[location] and move[1] == rooms[location]["item"]:
                inventory.append(move[1])
                print(f"{move[1]} picked up!")
                del rooms[location]["item"]
                show_status(location, inventory, rooms)
            else:
                print(f"Can't get {move[1]}!")

        elif move[0] == "inventory":
            print("Inventory:", inventory)

        elif move[0] == "help":
            show_instructions()

        elif move[0] == "quit":
            print("Thanks for playing!")
            break

        if "item" in rooms[location] and rooms[location]["item"] == "monster":
            print("A monster has got you... Game over!")
            break

        if location == "Garden" and "key" in inventory and "potion" in inventory:
            print("You escaped the house with the key and potion... You win!")
            break

if __name__ == "__main__":
    play_game()
