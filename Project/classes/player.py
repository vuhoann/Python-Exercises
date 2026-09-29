import random
class Player:
    def __init__(self,name,room):
        self.name = name
        self.items = []
        self.location = room
        self.life = 10

    def move(self,room):
        self.location = room
        life = random.randint(-3,1)
        self.life = self.life + life
        if life == -2:
            print("You encounter an enemy: your life - 2")
        elif life == -1:
            print("You encounter an obstacle: your life - 1")
        elif life == 1:
            print("You find some food: your life + 1")
        elif life == -3:
            print("You encounter a powerful enemy: your life - 3")

    def collect_item(self):
        if self.location.item != "":
            self.items.append(self.location.item)
            print(f"{self.location.item.name} added successfully! you receive {self.location.item.weight} life")
            self.life = self.life + self.location.item.weight
            self.location.item = ""
        else:
            print("No items collected")