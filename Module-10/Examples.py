# Example 1
class ShoppingList:
    def __init__(self):
        self.items = []
    def add(self,item):
        if not item in self.items:
            self.items.append(item)
    def print_item(self):
        for item in sorted(self.items):
            print(item)
    def longest_item(self):
        long = 0
        longest_item = ""
        for item in self.items:
            if longest_item == "" or long < len(item):
                longest_item = item
                long = len(item)
        print(f"The item has longest name is: {longest_item}")
        return longest_item
        
veget = ShoppingList()
veget.add("Tomato")
veget.add("Grapes")
veget.add("Broccoli")
veget.print_item()
veget.longest_item() 

# Example 2
class Car:
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour

class PaintShop:
    def paint(self, car, colour):
        car.colour = colour

car1=Car(123,"red")
print(f"{car1.number} - {car1.colour}")
colour1 = PaintShop()
colour1.paint(car1,"Blue")
print(f"{car1.number} - {car1.colour}")

# Example 3
class Visistor:
    def __init__(self,name :str ,height :int):
        self.name = name
        self.height = height
class Attraction:
    def __init__(self, name:str, height:int):
        self.list_visitor = []
        self.name = name
        self.height = height
    def check(self, person: Visistor):
        if self.height <= person.height:
            self.list_visitor.append(person)
            print(f"{person.name} get on board")
        else:
            print(f"{person.name} is toooo short")
    def __str__(self):
        for person in self.list_visitor:
            print(person.name)
        return(f"{self.name} ({len(self.list_visitor)} visitors)")

person1 = Visistor("Hoang",183)
person2 = Visistor("Thanh",158)
person3 = Visistor("Xin",118)
attraction1 = Attraction("RolerCoaster",120)
attraction1.check(person1)
attraction1.check(person2)
attraction1.check(person3)
print(attraction1)