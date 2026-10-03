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
        hp = random.randint(-3,1)
        self.hp = self.hp + hp
        if hp == -2:
            print(Fore.LIGHTRED_EX + "You encounter an enemy: your HP - 2")
        elif hp == -1:
            print(Fore.LIGHTRED_EX + "You encounter an obstacle: your HP - 1")
        elif hp == 1:
            print(Fore.LIGHTGREEN_EX + "You find some food: your HP + 1")
        elif hp == -3:
            print(Fore.LIGHTRED_EX + "You encounter a powerful enemy: your HP - 3")

    def collect_item(self):
        if self.location.item != "":
            self.items.append(self.location.item)
            print(Fore.LIGHTYELLOW_EX + f"{self.location.item.name} added successfully! you receive {self.location.item.weight} HP")
            self.hp = self.hp + self.location.item.weight
            self.location.item = ""
        else:
            print(Fore.LIGHTRED_EX + "No items collected")
        input("\nPress enter to continue.....")
        