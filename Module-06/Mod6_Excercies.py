# Excercise 1
import random
dice = int(input("How many dice to roll ? "))
total = 0
for i in range(1,dice+1):
    number = random.randint(1,6)
    total += number
print(total)

# Excercise 2
list_number =[]
while True:
    number = input("Enter a number: ")
    if number == "":
        break
    list_number.append(int(number))
list_number.sort(reverse=True)
print(list_number[0:5])

# Excercise 3
list_number =[]
number = int(input("Enter a number: "))
if number == 1:
    print(f"{number} is not a prime number")
else:
    for i in range(1,number+1):
        if number % i == 0:
            list_number.append(i)
    if len(list_number) > 2:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")

# Excercise 4
list_city = []
for i in range(1,6):
    city = input(f"Enter the name of the city {i} :")
    list_city.append(city)
for i in range(0,len(list_city)):
    print(list_city[i])
    