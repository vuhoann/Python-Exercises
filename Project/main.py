list_item = []
def add():
    item = input("Add an item: 1. Weapon, 2. Armor, 3. Potion, 4. Accessory ")
    if item == "1":
        list_item.append("Weapon")
        print("Item added successfully!")
    elif item == "2":
        list_item.append("Armor")
        print("Item added successfully!")
    elif item == "3":
        list_item.append("Potion")
        print("Item added successfully!")
    elif item == "4":
        list_item.append("Accessory")
        print("Item added successfully!")
    else:
        print("Invalid item")

def show():
    print(f"Items list:\n {list_item}")

def remove():
    remove_item = input("Enter an item to remove: 1. Weapon, 2. Armor, 3. Potion, 4. Accessory ")
    if remove_item == "1":
        if "Weapon" not in list_item:
            print("This item does not exist")
        else:
            list_item.remove("Weapon")
            print("Item removed successfully!")
    elif remove_item == "2":
        if "Armor" not in list_item:
            print("This item does not exist")
        else:
            list_item.remove("Armor")
            print("Item removed successfully!")
    elif remove_item == "3":
        if "Potion" not in list_item:
            print("This item does not exist")
        else:
            list_item.remove("Potion")
            print("Item removed successfully!")
    elif remove_item == "4":
        if "Accessory" not in list_item:
            print("This item does not exist")
        else:
            list_item.remove("Accessory")
            print("Item removed successfully!")
    else:
        print("Invalid item")

def check():
    item = input("Choose an item: 1. Weapon, 2. Armor, 3. Potion, 4. Accessory ")
    if item == "1":
        list_item.count("Weapon")
        print(f"Weapon: {list_item.count("Weapon")}")
    elif item == "2":
        list_item.count("Armor")
        print(f"Armor: {list_item.count("Armor")}")
    elif item == "3":
        list_item.count("Potion")
        print(f"Potion: {list_item.count("Potion")}")
    elif item == "4":
        list_item.count("Accessory")
        print(f"Accessory: {list_item.count("Accessory")}")
    else:
        print("Invalid item")
    

name = input("What is your name? ")
age = int(input("How old are you? "))
print ( "The player's name is: "+ name +"\nThe player's age is: "+ str(age))
if age < 12:
    print("You do not meet the minimum age requirement")
else:
    print("---------------------")
    print("*** Hello and welcome "+ name+" ***")
    while True:
        print("---------------------")
        print("----- Main Menu -----\n1. Add new item \n2. Show existing items \n3. Remove item \n4. Check amount item \n5. Quit ")
        command = input("Enter a command (1-4): ")
        if command == "lopeta":
            print("bye bye")
            break
        elif command == "1":
            add()
        elif command == "2":
            show()
        elif command == "3":
            remove()
        elif command == "4":
            check()            
        elif command == "5":
            print("Enter lopeta in command")
        else:
            print("Invalid command")

