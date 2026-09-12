
# Example 1
def sum(num1,num2):
    sum = num1 + num2
    return sum

number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))
print("sum is: ", sum(number_1,number_2))

# Example 2

def animal(animal_list):
    filtered_list= []
    for i in animal_list:
        if len(i) >= 5:
            filtered_list.append(i)
    print(animal_name)
    print(filtered_list)

animal_name = ["cat","dog","elephant","lion","giraffe"]
animal(animal_name)




