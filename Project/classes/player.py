# change text color using the colorama library
from colorama import Fore, Back, Style, init
# initialize colorama
init(autoreset=True)
import random

class Player:
    def __init__(self,name,room):
        self.name = name
        self.items = []
        self.location = room
        self.start_room = room
        self.hp = 10
        self.life = 3

    def move(self,room):
        self.location = room
        list_character=["Piccolo", "Cell", "Frieza", "Android 17", "Vegeta","Majin Buu", "Bulma", "Chi-Chi"]
        character = random.choice(list_character)
        if character == "Piccolo" or character == "Android 17":
            hp = -1
        elif character == "Vegeta" or character == "Frieza":
            hp = -2
        elif character == "Cell" or character == "Majin Buu":
            hp = -3
        elif character == "Bulma" or character == "Chi-Chi":
            hp = 1
        self.hp = self.hp + hp
        print(Fore.LIGHTCYAN_EX + f"You encounter {character}: your HP plus {hp}")

    def collect_item(self):
        if self.location.item != "":
            self.items.append(self.location.item)
            print(Fore.LIGHTYELLOW_EX + f"{self.location.item.name} added successfully! you receive {self.location.item.weight} HP")
            self.hp = self.hp + self.location.item.weight
            self.location.item = ""
        else:
            print(Fore.LIGHTRED_EX + "No items collected")
        input("\nPress enter to continue.....")
        