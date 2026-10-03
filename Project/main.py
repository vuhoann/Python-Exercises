from classes.player import Player
from classes.item import Item
from classes.room import Room
from file_handling import (save_game, load_game)
import os
# change text color using the colorama library
from colorama import Fore, Back, Style, init
# initialize colorama
init(autoreset=True)


# display greeting
def start(player):
    print(Fore.CYAN + Style.BRIGHT + f"\n\n\t\tHello and welcome {player.name}\n\n"
        "\tYou must collect all seven Dragon Balls\n\n"
        "-> Moves: \ttravel north, south, east or west\n"
        "-> Collect: \tadd Dragon Ball to your inventory\n\n"
        + Fore.RED +f" \t\tYou have 3 lives left \n\n") 
    input("Press enter to continue.....")
    clear()

# clear terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# moves
def move(direction):
    clear()
    if direction in player.location.location:
        print(Fore.GREEN + f"You move {direction} to {player.location.location[direction].name}")
        player.move(player.location.location[direction])
    else:
        print(Fore.RED + "You can't go that way")
    input("\nPress enter to continue.....")
    clear()

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
        exit()
        return True
    else:
        return False

# check HP
def HP():
    if player.hp <= 0:
        # return starting location
        player.location = player.start_room
        # minus player life
        player.life = player.life - 1
        # reset player HP
        player.hp = 10
        if len(player.items)>0:
            for i in player.items:
                player.hp += i.weight 
        clear()
        print(Style.BRIGHT + Fore.LIGHTRED_EX + "\n\n\t\tYou are out of HP\n\n")
        if player.life == 2:
            print(Style.BRIGHT + Fore.RED + "\t\tYou have 2 lives left\n\n")
            input("Press enter to play again!.....")
        elif player.life == 1:
            print(Style.BRIGHT + Fore.RED + "\t\tYou have 1 life left\n\n")
            input("Press enter to play again!.....")
        elif player.life == 0:
            input("Press enter to continue!.....")
        return True
    else: 
        return False

# check lose
def lose():
    if player.life <= 0:
        clear()
        print(Style.BRIGHT + Fore.RED + "\n\n\t\tGAME OVER")
        return True
    else:
        return False



# create item, room & player
def create_world():
    # create item
    item_1 = Item("Dragon Ball number 1",1)
    item_2 = Item("Dragon Ball number 2",4)
    item_3 = Item("Dragon Ball number 3",1)
    item_4 = Item("Dragon Ball number 4",3)
    item_5 = Item("Dragon Ball number 5",2)
    item_6 = Item("Dragon Ball number 6",2)
    item_7 = Item("Dragon Ball number 7",1)
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
    room_1.add_direction("west",room_2,"north",room_4)
    room_2.add_direction("east",room_1,"south",room_3,"north",room_9)
    room_3.add_direction("north",room_2)
    room_4.add_direction("south",room_1,"east",room_5,"north",room_6,"west",room_9)
    room_5.add_direction("west",room_4)
    room_6.add_direction("south",room_4,"north",room_7,"west",room_8)
    room_7.add_direction("south",room_6)
    room_8.add_direction("east",room_6,"west",room_13,"south",room_11)
    room_9.add_direction("north",room_11,"west",room_10,"east",room_4,"south",room_2)
    room_10.add_direction("east",room_9,"west",room_15)
    room_11.add_direction("south",room_9,"west",room_12,"north",room_8)
    room_12.add_direction("east",room_11,"north",room_13,"west",room_14)
    room_13.add_direction("south",room_12,"east",room_8)
    room_14.add_direction("east",room_12,"south",room_15)
    room_15.add_direction("north",room_14,"east",room_10,"south",room_16)
    room_16.add_direction("north",room_15)
    # room dict:
    rooms = {}
    for room in [room_1,room_2,room_3,room_4,room_5,room_6,room_7,room_8,room_9,room_10,room_11,room_12,room_13,room_14,room_15,room_16]:
        rooms[room.name] = room
    return rooms
# load / save game
def main():
    while True:
        clear()
        set_up = input("--------------------------\n1. Load game \n2. New game\n")
        if set_up == "1":
            rooms = create_world()
            player = load_game(rooms)
            if player:
                print("Welcome back" + Fore.LIGHTBLUE_EX +  f" {player.name}")
                input("Press enter to continue!.....")
                return player, rooms
            else:
                clear()
                print(Fore.RED+"\nNo save data found")
                input("Press enter to continue!.....")
        elif set_up == "2":
            clear()
            name = input("What is your name? ")
            age = input("How old are you? ")
            if name == "" or age == "":
                print(Fore.RED + "\nPlease enter your name and age")
                input("Press enter to continue!.....")
            elif int(age) < 12:
                clear()
                print(Fore.RED + Style.BRIGHT + "\nYou do not meet the minimum age requirement")
                input("Press enter to continue!.....")
            else:
                clear()
                rooms = create_world()
                player = Player(name, rooms["Kame House"])
                start(player)
                return player, rooms    
        else:
            print(Fore.RED + "Invalid command")

# main code
player, rooms = main()
while True:
    # check lose
    if lose():
        break
    # main game loop
    while True:
        clear()
        # check win 
        if win():
            break
        # check HP
        if HP():
            break
        # main menu
        print("--------------------------")
        print("Player:" + Fore.LIGHTBLUE_EX + f"{player.name}")
        print("Current location:" + Fore.LIGHTBLUE_EX + f"{player.location.name}")
        show_inventory()
        show_item()
        print(f"Your HP:" + Fore.RED + f" {player.hp}")
        print("--------------------------\n1. Collect \t2. Go North \t7. Save Game \n3. Go South \t4. Go West \n5. Go East \t6. Quit ")
        command = input("Enter a command (1-6): ")
        if command == "1":
            clear()
            player.collect_item()
            clear()
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
            command = input("Enter lopeta in command: \n")
            if command == "lopeta":
                print("Bye bye")
                exit()
            else: 
                input("Invalid command")
        elif command == "7":
            save_game(player, rooms)
            input("Press enter to continue!.....")
        else:
            clear()
            print(Fore.RED + "Invalid command")
            input("Press enter to continue!.....")
                
