
#example 1

Age = int(input ("How old are you ?"))

if Age >= 18:
    print("Yon are old enough to vote in Finnish parliamentary")
else:
    print(f"You need {18-Age} years to reach legal age and the right to vote")

#example 2

Elec_consump = float (input("What is your electricity consumption (kWh)? :"))

if Elec_consump <=50:
    print (f"Your electricity cost is: €{Elec_consump*0.1:.2f}")
elif Elec_consump <=200:
    print (f"Your electricity cost is: €{(50*0.1 + (Elec_consump-50)*0.08):.2f}")
else:
    print (f"Your electricity cost is: €{(50*0.1 + 150*0.08 + (Elec_consump-200)*0.06):.2f}")

#example 3

Math = float(input("What is your mathematics grade :"))
Physic = float(input("What is your physics grade :"))
Chemistry = float(input("What is your chemistry grade :"))


if Math < 50 or Physic < 50 or Chemistry < 50:
    print ("you cannot receive any scholarship")
elif Math >= 90 and Physic >= 90 or Chemistry >=95:
    print("you can receive a scholarship")
else:
    print("you cannot receive a scholarship")

#example 4

letter = input("Input a letter of the alphabet:")

if letter == "a" or letter == "e" or letter == "i" or letter== "o" or letter == "u":
    print("The entered letter is a vowel")
elif letter == "y":
    print("Sometimes y is a vowel and sometimes y is a consonant")
else:
    print("the entered letter is a consonant")