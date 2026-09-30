class Room:
    def __init__(self,name,item = ""):
        self.name = name
        self.item = item
        self.location = {}
    def add_direction(self,direction1="",room1 ="",direction2="",room2 ="",direction3="",room3 ="",direction4="",room4 =""):
        self.location[direction1] = room1
        self.location[direction2] = room2
        self.location[direction3] = room3
        self.location[direction4] = room4
