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
class Race:
    def __init__(self,name,distance,car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list
    def hour_passes(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
    def print_status(self):
        print(f"{'Registration':<15} | {'Max Speed':<15} | {'Current Speed':<15} | {'Distance':<15}")
        print("---------------------------------------------------------------")
        self.car_list.sort(key=lambda car: car.travelled_distance, reverse=True)
        for car in self.car_list:
            print(f"{car.registration_number:<15} | {car.maximum_speed:<15} | {car.current_speed:<15} | {car.travelled_distance:<15}")
    def race_finished(self):
        for car in self.car_list:
            if car.travelled_distance >= self.distance:
                return True
        return False
    

num = 0
list_car =[]
regis = 1
while num < 10:
    regist = "ABC-"+ str(regis)
    speed = random.randint(100,200)
    list_car.append(Car(regist,speed))
    num += 1
    regis +=1

race_1 = Race("Viet Nam",8000, list_car)
hour = 0
while True:
    if race_1.race_finished() == True:
        print(f"\nRace finished in {hour} hours")
        race_1.print_status()
        break   
    else:
        race_1.hour_passes()
        hour += 1
        if hour % 10 == 0:
            print(f"\nRace in {hour} hours") 
            race_1.print_status()