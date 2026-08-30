
#Excercise 1

length = float(input("What is the length of a zander (cm): "))
if length < 42:
    print(f"The zander does not fulfill the size limit \nplease release it back into the lake \nThe fish is {(42-length):.2f} below the size limit")
else:
    print("The zander meets the size limit")

#Excercise 2

cabin_class = input("Enter the cabin class: ")
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck")
else:
    print("Invalid cabin class")

#Excercise 3

gender = input("What is your gender? ")
hemoglobin = float(input("What is your hemoglobin value (g/l)"))

if gender == "female" and hemoglobin <117:
    print("Your hemoglobin value is low")
elif gender == "female" and hemoglobin <=155:
    print("Your hemoglobin value is normal")
elif gender == "female" and hemoglobin  >155:
    print("Your hemoglobin value is high")
elif gender == "male" and hemoglobin <134:
    print("Your hemoglobin value is low")
elif gender == "male" and hemoglobin <=167:
    print("Your hemoglobin value is normal")
elif gender == "male" and hemoglobin  >167:
    print("Your hemoglobin value is high")

#Excercise 4

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print("The input year is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("The input year is a leap year")
else:
    print("The input year is not a leap year")

