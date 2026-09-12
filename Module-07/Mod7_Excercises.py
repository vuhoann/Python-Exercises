# Excercise 1
import random
def roll():
    dice = random.randint(1,6)
    return dice

while True:
    result = roll()
    if result != 6:
        print(result)
    else:
        print(result)
        break

# Excercise 2
import random
def roll(side):
    dice = random.randint(1,side)
    return dice

side = int(input("Enter a number of side: "))
while True:
    result = roll(side)
    if result != side:
        print(result)
    else:
        print(result)
        break

# Exercise 3
def quantity(gallon):
    litre = gallon * 3.785411784
    return litre
while True:
    gasoline = float(input("Enter the quantity of gasoline in US gallon: "))
    if gasoline < 0:
        print("Negative value")
        break
    else:
        print(f"The quantity of gasoline in litre is: {quantity(gasoline):.3f}")

# Excercise 4
def sum(list_int):
    total = 0
    for i in list_int:
        total += i
    return total

num_list = [21,43,5,31,-3,0,78]
result = sum(num_list)
print(f"The sum of all the numbers is: {result}")

# Excercise 5
def even(original_list):
    second_list = []
    for i in original_list:
        if i % 2 == 0:
            second_list.append(i)
    return second_list

number_list = [21,43,5,31,-3,0,78,22,45,66]
result_ = even(number_list)
print(number_list)
print(result_)

# Excercise 6
def pizza(diameter,price):
    unitprice = price / (diameter**2/4)
    return unitprice

size_1 = float(input("Enter the diameter of the 1st pizza in cm: "))
price_1 = float(input("Enter the price of the 1st pizza in €: "))
size_2 = float(input("Enter the diameter of the 2nd pizza in cm: "))
price_2 = float(input("Enter the price of the 2nd pizza in €: "))
pizza_1 = pizza(size_1,price_1)
pizza_2 = pizza(size_2,price_2)
if pizza_1 < pizza_2:
    print(f"Pizza 1 is better value than pizza 2 {(((pizza_2-pizza_1)/pizza_2)*100):.2f}%")
else:
    print(f"Pizza 2 is better value than pizza 1 {(((pizza_1-pizza_2)/pizza_1)*100):.2f}%")