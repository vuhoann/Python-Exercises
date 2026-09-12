# excercise 1
season = ("spring","summer","autumn","winter")
num = int(input("Enter a number of a month (1-12): "))
if num in (3,4,5):
    current_season = season[0]
elif num in (6,7,8):
    current_season = season[1]
elif num in (9,10,11):
    current_season = season[2]
elif num in (12,1,2):
    current_season = season[3]
else:
    print("invalid month")   
print(f"month {num} is in {current_season}")

# Excercise 2
name_list = set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    else:
        if name in name_list:
            print("Existing name")
        else:
            name_list.add(name)
            print("New name")
for i in name_list:
    print(i)

# Excercise 3
data = []
ICAO_code = set()
def new(icao, name):
    if icao in ICAO_code:
        print(f"The ICAO code {icao} already exists in the list")
    else:
        airport = {
            "ICAO":icao,
            "Name":name
        }
        data.append(airport)
        ICAO_code.add(icao)
        print("New airport was added")
def fetch(icao):
    for i in data:
        if i["ICAO"] == icao:
            print(f"The ICAO code {icao} belongs to {i['Name']} airport")
            return
    print(f"The ICAO code {icao} does not exist")

while True:
    print("-------------")
    print("Main program")
    print("a. enter a new airport")
    print("b. fetch an existing airport")
    print("c. quit")
    command = input("Enter a command a,b or c: ")
    if command == "a":
        print("-------------")
        icao = input("Enter a ICAO code: ")
        name = input("Enter a name of airport: ")
        new(icao,name)
    elif command == "b":
        print("-------------")
        icao_fetch = input("Enter a ICAO code: ")
        fetch(icao_fetch)
    elif command == "c":
        print("The program was closed")
        break
    else:
        print("invalid command")
