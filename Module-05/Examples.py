# Example 1
number = int(input("Enter a number: "))
even_number = 0
if number <= 0:
    print("Error message")
else:
    while even_number <= number:
        if even_number % 2 == 0:
            print(even_number)
        even_number += 1

# Example 2
sum_number = 0
count = 0
while sum_number < 1000:
    number = int(input("Enter a number:"))
    sum_number += number
    count += 1
print(sum_number)
print(count)

# Example 3
height = float(input("Enter the height of the object (m) : "))
distance = 0
time = 0
while height - distance >= 0:
    distance = 0.5 * 9.81 * time**2
    time += 0.1
    print(f"Current Height {(height-distance):.2f}")
print(f"Total time (s): {time:.2f}")

# Example 4
first_number = 1
while first_number <= 5:
    second_number = 1
    while second_number <= 5:
        print(f"{first_number} is {second_number} equals {first_number*second_number}")
        second_number += 1
    first_number += 1

# Example 5
while True:
    number = int(input("Enter a number: "))
    if number <= 0:
        print(" The execution ends")
        break

    factorial = 1
    new = 1
    while new <= number:
        factorial *=new
        new += 1
    print(f"The factorial of the number {number} is {factorial}")
