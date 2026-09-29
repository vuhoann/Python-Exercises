# Excercise 1

class Publication:
    total_publication = 0
    def __init__(self,name):
        Publication.total_publication = Publication.total_publication + 1
        self.publication_number = Publication.total_publication
        self.name = name
    def print_information(self):
        print(f"{self.publication_number}: {self.name}")
class Book(Publication):
    def __init__(self,name,author,page):
        self.author = author
        self.page = page
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}, {self.page} pages")

class Magazine(Publication):
    def __init__(self,name,chief):
        self.chief = chief
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief}") 


e1 = Magazine("Donald Duck","Aki Hyyppa")
e2 = Book("Compartment No.6", "Rosa Liksom", 192)
e1.print_information()
e2.print_information()   

# Excercise 2
import random
class Car:
    def __init__(self,regist_number:str,max_speed:float):
        self.registration_number = regist_number
        self.maximum_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def __str__(self):
        return(f"Car {self.registration_number}: \n"
               f"Max speed = {self.maximum_speed} \n"
               f"Current speed = {self.current_speed} \n"
               f"Distance = {self.travelled_distance}")
    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed >=self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed <= 0:
            self.current_speed = 0
    def drive(self, hour):
        self.travelled_distance += self.current_speed*hour
class ElectricCar(Car):
    def __init__(self,regist_number,max_speed,battery_capacity):
        super().__init__(regist_number,max_speed)
        self.capacity = battery_capacity
    def __str__(self):
        return(f"{super().__str__()} \nBattery capacity: {self.capacity}")
class GasolineCar(Car):
    def __init__(self,regist_number,max_speed,volume):
        super().__init__(regist_number,max_speed)
        self.volume = volume
    def __str__(self):
        return(f"{super().__str__()} \nVolume of the tank: {self.volume}")

electric_car = ElectricCar("ABC-15",180,52.5)
gasoline_car = GasolineCar("ABC-123",165,32.3)
electric_car.accelerate(random.randint(50,100))
gasoline_car.accelerate(random.randint(30,120))
electric_car.drive(3)
gasoline_car.drive(3)
print(electric_car)
print(gasoline_car)
