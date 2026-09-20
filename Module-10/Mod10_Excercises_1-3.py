# Excercise 1,2 & 3
class Elevator:
    def __init__(self,num_bot,num_top):
        self.num_bot = num_bot
        self.num_top = num_top
        self.current = num_bot
    def go_to_floor(self,floor):
        if floor > self.num_top or floor < self.num_bot:
            print("Invalid floor")
        else:
            while self.current < floor:
                self.floor_up()
            while self.current > floor:
                self.floor_down()   
    def floor_up(self):
        self.current +=1
        print(f"Elevator is at floor: {self.current}")
    def floor_down(self):
        self.current -=1
        print(f"Elevator is at floor: {self.current}")


class Building:
    def __init__(self,num_bot,num_top,num_ele):
        self.num_bot = num_bot
        self.num_top = num_top
        self.num_ele = num_ele
        self.list_elevator = []
        for i in range(num_ele):
            self.list_elevator.append(Elevator(num_bot,num_top))
    def run_elevator(self,ele_num,floor):
        if ele_num > len(self.list_elevator) or ele_num < 1:
            print("Invalid elevator")
        else:
            print(f"Running elevator {ele_num}")
            select = self.list_elevator[ele_num-1]
            select.go_to_floor(floor)
    def fire_alarm(self):
        print(f"FIRE! Running all elevators")
        for i in range(len(self.list_elevator)):
            self.run_elevator(i+1,self.num_bot)
    
h = Elevator(-2,20)
print(f"Elevator is at floor: {h.current}")
h.go_to_floor(5)
h.go_to_floor(10)
h.go_to_floor(0)
b = Building(0,20,3)
b.run_elevator(1,17)
b.run_elevator(2,10)
b.run_elevator(3,2)
b.fire_alarm()

