# Example 1
fruit = {}
for i in range(3):
    name = input("Enter the name of fruit: ")
    amount = input("Enter the amount of fruit in kilogram: ")
    fruit[name] = amount + " kg"
print(fruit)

# Example 2
numlist = []
while True:
    num = float(input("Enter a number: "))
    if num == 0:
        break
    else:
        numlist.append(num)
# print(numlist)
new_set = set(numlist)
# print(new_set)
unique_list = list(new_set)
print(unique_list)

# Excercise 3
phonebook = []
def add(name, id, dob, phone):
    contact = {
        "name": name,
        "id": id,
        "dob": dob,
        "phone": phone
    }
    phonebook.append(contact)
def search(name):
    for i in phonebook:
        if i["name"] == name:
            print (f"{name}'s id: {i['id']}, date-of-birth: {i['dob']}, phone number: {i['phone']}")
            return
    print ("contact name doesn't exist")
while True:
    print("--------------")
    print("Here is a menu:")
    print("a. add a new contact")
    print("b. search for an existing contact")
    print("c. quit")
    command = input("select a, b or c: ")
    if command == "a":
        print("--------------")
        name = input("Add a name: ")
        id = input("Add an id: ")
        dob = input("Add a date-of-birth: ")
        phone = input("Add a phone number: ")
        add(name,id,dob,phone)
        print("contact was added")
    elif command == "b":
        print("--------------")
        name = input("Search a name: ")
        search(name)
    elif command == "c":
        print("bye bye")
        break
    else: 
        print("command is incorrect")