import math

radius = float(input("Enter the radius of the circle:"))
side = float(input("Enter the side lenght of the square:"))

circle_area = math.pi * radius**2
square_area = side**2

print(f"Area of the circle is {circle_area:.2f}")
print(f"Area of the square is {square_area:.2f}")

#---

Banana = float(input ("Enter the amount of bananas (kg)"))
Apple = float(input ("Enter the amount of apples (kg)"))
Orange = float(input ("Enter the amount of orange (kg)"))

Banana_price = Banana*2.85
Apple_price = Apple*3.15
Orange_price = Orange*4.05
Total_price = Banana_price+Apple_price+Orange_price

print ("Shopping summary:" + f"\nBananas: €{Banana_price:.2f}"+ f"\nApples: €{Apple_price:.2f}"+ f"\nOranges: €{Orange_price:.2f}" +f"\nTotal: €{Total_price:.2f}")

#---

import random

first_dice = random.randint(1,6)
second_dice = random.randint(1,20)

print (f"The total sum of both dice {first_dice+second_dice}")

