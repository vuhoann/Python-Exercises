class Player:
    def __init__(self,name,room):
        self.name = name
        self.items = []
        self.location = room
    def move(self,room):
        self.location = room
    def collect_item(self):
        if self.location.item != "":
            self.items.append(self.location.item)
            print(f"{self.location.item.name} added successfully!")
            self.location.item = ""
        else:
            print("No items collected")

class Room:
    def __init__(self,name,item = ""):
        self.name = name
        self.item = item

class Item:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return (f"-{self.name} ({self.weight} slots)")
