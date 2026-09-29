class Room:
    def __init__(self,name,item = ""):
        self.name = name
        self.item = item
        self.location = {}
    def add_direction(self,direction,room):
        self.location[direction] = room