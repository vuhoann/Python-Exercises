
from gameclasses import Player, Item, Room

def move():
    print("---------------------")
    room = input("Choose a room: \n1. Great_Hall \n2. Chamber \n3. Dungeon \n4. Armoury \n5. Chapel \n")
    if room == "1":
        player.move(room_1)
    elif room == "2":
        player.move(room_2)
    elif room == "3":
        player.move(room_3)
    elif room == "4":
        player.move(room_4)
    elif room == "5":
        player.move(room_5)
    else:
        print("Invalid room")



name = input("What is your name? ")
age = int(input("How old are you? "))
print ( "The player's name is: "+ name +"\nThe player's age is: "+ str(age))
if age < 12:
    print("You do not meet the minimum age requirement")
else:
    print("--------------------------")
    print("*** Hello and welcome "+ name +" ***")
    item_1 = Item("Weapon",3)
    item_2 = Item("Armor",5)
    item_3 = Item("Potion",1)
    item_4 = Item("Ring",2)
    room_1 = Room("Great_Hall",item_4)
    room_2 = Room("Chamber")
    room_3 = Room("Dungeon",item_2)
    room_4 = Room("Armoury",item_1)
    room_5 = Room("Chapel",item_3)
    player = Player(name,room_1)
    while True:
        print("---------------------")
        print(f"Player: {player.name}")
        print(f"Current location: {player.location.name}")
        if player.location.item == "":
            print(f"No item in room")
        else:
            print(f"Item in room: {player.location.item.name}")
        print("---------------------\n1. Collect an item \n2. Move to another room \n3. Show Your Inventory \n4. Quit ")
        command = input("Enter a command (1-4): ")
        if command == "lopeta":
            print("Bye bye")
            break
        elif command == "1":
            player.collect_item()
        elif command == "2":
            move()
        elif command == "3":
            print("---------------------")
            if player.items != []:
                print("Your inventory: ")
                for item in player.items:
                    print(item)
            else:
                print("Your inventory is empty")
        elif command == "4":
            print("Enter lopeta in command")
        else:
            print("Invalid command")

