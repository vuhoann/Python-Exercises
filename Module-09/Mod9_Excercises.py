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
    
# # Excercise 1-3
# new_car = Car("ABC-123",142)
# print(new_car)
# new_car.accelerate(30)
# new_car.accelerate(70)
# new_car.accelerate(50)
# print(f"Current speed is: {new_car.current_speed}")
# new_car.accelerate(-200)
# print(f"Final speed is: {new_car.current_speed}")
# new_car.accelerate(60)
# new_car.drive(4)
# print(f"Travelled distance is: {new_car.travelled_distance}")
# new_car.drive(6)
# print(f"Travelled distance is: {new_car.travelled_distance}")
# # Excercise 4
num = 0
list_car =[]
regis = 1
while num < 10:
    regist = "ABC-"+ str(regis)
    speed = random.randint(100,200)
    list_car.append(Car(regist,speed))
    num += 1
    regis +=1
race = 0
while race != 1:
    for car in list_car:
        car.accelerate(random.randint(-10,15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race = 1
            list_car.sort(key=lambda car: car.travelled_distance, reverse=True)
            print("The race ended")
            print("--------------")
            for car in list_car:
                print(car)
            
    
