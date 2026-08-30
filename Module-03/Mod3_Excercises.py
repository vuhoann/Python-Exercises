
#Excercise 1

name = input ("What is your name? ")
print("Hello, "+ name + "!")

#Excercise 2

import math
radius = float(input("Enter the radius of a circle: "))
print(f"The area of the circle is: {math.pi*radius**2:.2f}")

#Excercise 3

length = float(input("What is the length of a rectangle: "))
width = float(input("What is the width of a rectangle: "))
print(f"The perimeter of the rectangle is: {((length+width)*2):.2f} \nThe area of the rectangle is: {length*width:.2f}")

#Excercise 4
number_1 = int(input("Enter 1st integer number: "))
number_2 = int(input("Enter 2nd integer number: "))
number_3 = int(input("Enter 3rd integer number: "))
print(f"The sum of the numbers is: {number_1+number_2+number_3} \nThe product of the numbers is: {number_1*number_2*number_3} \nThe average of the numbers is: {(number_1+number_2+number_3)/3:.2f}")

#Excercise 5
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))

grams = talent*20*32*13.3 + pound*32*13.3 + lot*13.3
kilograms = grams // 1000

print(f"The weight in modern units: {kilograms} kilograms and {(grams-kilograms*1000):.2f} grams")

#Excercise 6

import random
number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)
print(f"A 3-digit code is: {number1}{number2}{number3}" )

number4 = random.randint(1,6)
number5 = random.randint(1,6)
number6 = random.randint(1,6)
number7 = random.randint(1,6)
print(f"A 4-digit code is: {number4}{number5}{number6}{number7}" )