name = input("What is your name? ")
age = int(input("How old are you? "))
print ( "The player's name is: "+ name +"\nThe player's age is: "+ str(age))
if age < 12:
    print("You do not meet the minimum age requirement")
else:
    print("***Hello and welcome "+ name+"***")
    print("----- Main Menu -----\nStart Game \nLoad Game \nGame Mode \nSetting \nQuit ")
    command = input("Enter a command: ")
    while command != "lopeta":
        if command == "start":
            print("----- The game is starting -----")
        elif command == "load":
            print("----- The game is loading -----")
        elif command == "mode":
            print("----- Mode -----")
        elif command == "set":
            print("----- Setting Menu -----")
        elif command == "quit":
            print("Enter lopeta in command")
        print("----- Main Menu -----\nStart Game \nLoad Game \nGame Mode \nSetting \nQuit ")
        command = input("Enter a command: ")
    else:
        print("Goodbye")