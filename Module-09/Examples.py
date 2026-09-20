# Example 1
class Coffee:
    coffee_type = {
        "Black": 5,
        "Latte": 7,
        "Mochi": 11,
        "Capuchino": 9
    }
    defaut_price = 7
    def __init__(self,type:str,number:int):
        self.type = type
        self.number = number
        if self.type in self.coffee_type:
            self.price = self.coffee_type[type]
        else:
            self.price = self.defaut_price
    def total_price(self):
        return self.number*self.price
    def price_vat(self):
        return self.total_price()*(1+(13.5/100))
    def add_cups(self,extra):
        self.number = self.number + extra
        return self.total_price()
    def __str__(self):
        return(f"Coffee type: {self.type} \n"
               f"Number of cups: {self.number} \n"
               f"Price per cup: {self.price} \n"
               f"Total price: {self.total_price()} \n"
               f"Total price with VAT: {self.price_vat()}")

order1 = Coffee("Black",4)
print(order1)
order2 = Coffee("Milk",5)
print(order2)
order3 = Coffee("Mochi",3)
print(order3)
order1.add_cups(3)
print(order1)

# Example 2
class People:
    def __init__(self,name:str,height:int):
        self.name = name
        self.height = height
    def __str__(self):
        return(f"{self.name} is {self.height}cm tall")
class Room:
    def __init__(self):
        self.people = []
    def add(self, person : People):
        self.people.append(person)
    def is_empty(self):
        return len(self.people) == 0
    def print_info(self):
        print(f"There are {len(self.people)} people in the classroom")
        for i in self.people:
            print(f"- {i}")
    def check_tallest(self):
        tallest_per = None
        height_tallest = 0
        for i in self.people:
            if tallest_per == None or height_tallest < i.height:
                tallest_per = i
                height_tallest = i.height
        return tallest_per
    def remove_tallest(self):
        tallest_per = self.check_tallest()
        if tallest_per:
            self.people.remove(tallest_per)
        return tallest_per

room1 = Room()
print(f"Whether the room is empty: {room1.is_empty()}")
print(f"The tallest person is: {room1.check_tallest()}")
room1.add(People("Hoang", 180))
room1.add(People("Thanh", 158))
room1.add(People("Xin", 164))
room1.print_info()
print(f"Whether the room is empty: {room1.is_empty()}")
print(f"The tallest person is: {room1.check_tallest()}")
room1.remove_tallest()
room1.print_info()
print(f"The tallest person is: {room1.check_tallest()}")

# Example 3
class Task:
    def __init__(self,name,priority = "normal"):
        self.name = name
        self.priotiry = priority
    def __str__(self):
        return(f"Task {self.name} is {self.priotiry} priority")
class ToDoList:
    def __init__(self):
        self.task = []
    def add(self, task: Task):
        self.task.append(task)
    def show(self):
        if len(self.task) == 0:
            print("You are free! To-do-list is empty")
        else:
            for i in self.task:
                print(i)
    def remove(self,remove_task):
        for i in self.task:
            if i.name == remove_task:
                self.task.remove(i)
                print(f"{remove_task} has been removed")
                return
        print(f"{remove_task} is not on to-do-list")
to_do_list = ToDoList()
while True:
    print("---------")
    print("To-do-list")
    print("1. Add a new task")
    print("2. Show the task with priority")
    print("3. Remove a task")
    print("4. Quit")
    command = int(input("Choose 1-4: "))
    if command == 1:
        task_name = input("Enter a task name: ")
        task_priority = input("Enter a priority: ")
        to_do_list.add(Task(task_name,task_priority))
    elif command == 2:
        to_do_list.show()
    elif command == 3:
        task_remove = input("Enter a task you want to remove: ")
        to_do_list.remove(task_remove)
    elif command == 4:
        print("Bye Bye")
        break
    else:
        print("Invalid command")
