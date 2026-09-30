from classes.player import Player
from classes.item import Item
from classes.room import Room
import os
# change text color using the colorama library
from colorama import Fore, Back, Style, init
# initialize colorama
init(autoreset=True)

# moves
def move(direction):
    clear()
    if direction in player.location.location:
        print(Fore.GREEN + f"You move {direction} to {player.location.location[direction].name}")
        player.move(player.location.location[direction])
    else:
        print(Fore.RED + "You can't go that way")

# display staring menu
def start():
    print(Fore.CYAN + Style.BRIGHT + f"\n\n\t\tHello and welcome {name}\n\n"
          "\tYou must collect all seven Dragon Balls\n\n"
          "Moves: \tgo {direction} (travel north, south, east or west)\n"
          "\t collect: (add Dragon Ball to your inventory)\n\n ")
    input("Press enter to continue.....")

# clear terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# show inventory
def show_inventory():
    if player.items != []:
        print("Your inventory: ")
        for item in sorted(player.items, key = lambda x: x.name):
            print(Fore.YELLOW + f"{item}")
    else:
        print("Your inventory is empty")   
        
# show item in room
def show_item():
    if player.location.item == "":
        print(f"No Dragon Ball here")
    else:
        print("Item in room:" + Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"{player.location.item.name}")

# check win game
def win():
    if len(player.items) == 7:
        clear()
        print(Style.BRIGHT + Fore.YELLOW + "\n\n\t\tCongratulation! You won - let make a wish")
        return True
    else:
        return False

# check lose game
def lose():
    if player.life <= 0:
        clear()
        print(Style.BRIGHT + Fore.RED + "\n\n\t\tGame over")
        return True
    else: 
        return False

# main code
name = input("What is your name? ")
age = int(input("How old are you? "))
if age < 12:
    clear()
    print("You do not meet the minimum age requirement")
else:
    clear()
    start()
    # create item
    item_1 = Item("Dradon Ball number 1",2)
    item_2 = Item("Dradon Ball number 2",5)
    item_3 = Item("Dradon Ball number 3",2)
    item_4 = Item("Dradon Ball number 4",4)
    item_5 = Item("Dradon Ball number 5",3)
    item_6 = Item("Dradon Ball number 6",3)
    item_7 = Item("Dradon Ball number 7",2)
    # create rooms
    room_1 = Room("Kame House")
    room_2 = Room("Frypan Mountain")
    room_3 = Room("Papaya Island",item_4)
    room_4 = Room("Satan City")
    room_5 = Room("East Capital",item_6)
    room_6 = Room("Jingeru Village")
    room_7 = Room("Muscle Tower",item_5)
    room_8 = Room("North Capital")
    room_9 = Room("Pilaf castle")
    room_10 = Room("Baseru City",item_1)
    room_11 = Room("Central Capital")
    room_12 = Room("Ginger Town")
    room_13 = Room("Yunzabit Heights",item_2)
    room_14 = Room("Karin's Holy Ground")
    room_15 = Room("Red Ribbon Army HQ",item_3)
    room_16 = Room("Nama Village",item_7)
    # add direction
    room_1.add_direction("west",room_2)
    room_1.add_direction("north",room_4)
    room_2.add_direction("east",room_1)
    room_2.add_direction("south",room_3)
    room_2.add_direction("north",room_9)
    room_3.add_direction("north",room_2)
    room_4.add_direction("south",room_1)
    room_4.add_direction("east",room_5)
    room_4.add_direction("north",room_6)
    room_4.add_direction("west",room_9)
    room_5.add_direction("west",room_4)
    room_6.add_direction("south",room_4)
    room_6.add_direction("north",room_7)
    room_6.add_direction("west",room_8)
    room_7.add_direction("south",room_6)
    room_8.add_direction("east",room_6)
    room_8.add_direction("west",room_13)
    room_8.add_direction("south",room_11)
    room_9.add_direction("north",room_11)
    room_9.add_direction("west",room_10)
    room_9.add_direction("east",room_4)
    room_9.add_direction("south",room_2)
    room_10.add_direction("east",room_9)
    room_10.add_direction("west",room_15)
    room_11.add_direction("south",room_9)
    room_11.add_direction("west",room_12)
    room_11.add_direction("north",room_8)
    room_12.add_direction("east",room_11)
    room_12.add_direction("north",room_13)
    room_12.add_direction("west",room_14)
    room_13.add_direction("south",room_12)
    room_13.add_direction("east",room_8)
    room_14.add_direction("east",room_12)
    room_14.add_direction("south",room_15)
    room_15.add_direction("north",room_14)
    room_15.add_direction("east",room_10)
    room_15.add_direction("south",room_16)
    room_16.add_direction("north",room_15)
    # Create player
    player = Player(name,room_1)

    # main game loop
    while True:
        # check win lose
        if win():
            break
        if lose():
            break
        # main menu
        print("--------------------------")
        print("Player:" + Fore.LIGHTBLUE_EX + f"{player.name}")
        print("Current location:" + Fore.LIGHTBLUE_EX + f"{player.location.name}")
        show_inventory()
        show_item()
        print(f"Your life:" + Fore.RED + f" {player.life}")
        print("--------------------------\n1. Collect \t2. Go North \n3. Go South \t4. Go West \n5. Go East \t6. Quit ")
        command = input("Enter a command (1-6): ")
        if command == "lopeta":
            print("Bye bye")
            break
        elif command == "1":
            clear()
            player.collect_item()
        elif command == "2":
            move("north")
        elif command == "3":
            move("south")
        elif command == "4":
            move("west")
        elif command == "5":
             move("east")
        elif command == "6":
            clear()
            print("Enter lopeta in command")
        else:
            print("Invalid command")

