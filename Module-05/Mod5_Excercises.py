# Excercise 1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

# Excercise 2 (OPTION)
while True:
    inch = float(input("Enter the length (inch): "))
    if inch < 0:
        print("The program ends")
        break
    else:
        centimeter = inch*2.54
        print(f"The lenght in centimeter is: {centimeter:.2f}cm")

# Excercise 2
inch = float(input("Enter the length (inch): "))
while inch >= 0:
    centimeter = inch*2.54
    print(f"The lenght in centimeter is: {centimeter:.2f}cm")
    inch = float(input("Enter the length (inch): "))

# Excercise 3
number = input("Enter a number: ")
smallest = float(number)
largest = float(number)
while number != "":
    num = float(number)
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    number = input("Enter a number: ")
print(f"The smallest number is {smallest} \nThe largest number is {largest}")

# Excercise 4
import random
number = int(input("Enter a number from 1 to 10: "))
right_number = random.randint(1,10)
while number != right_number:
    if number < right_number:
        print ("Too low")
    elif number > right_number:
        print ("Too high")
    number = int(input("Enter a number from 1 to 10: "))
print("Correct")

# Excercise 5
correct_username = "python"
correct_password = "rules"
attemp = 1
while attemp <= 5:
    username = input("Enter a username: ")
    password = input("Enter a password: ") 
    if username != correct_username or password !=correct_password:
        print ("Username or password is incorrect")
        attemp += 1
    else:
        print ("Welcome")
        break
else:
    print ("Access denied")   

# Excercise 6
import random
N_point = int(input("How many random points to generate: "))
n_point =0
number = 0
while number <= N_point:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2) < 1:
        n_point += 1
    number += 1
print (f" value of pi: {4*n_point/N_point}")


