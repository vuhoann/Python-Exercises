# Example 1
name = input("What is your name ? ")
for i in name:
    print(i)

# Example 2
number = int(input("Enter a number: "))
if number <= 0:
    print("Error")
else:
    # use if to check
    for i in range(0,number+1):
        if i % 2 == 0:
            print(i)
    # use steps
    for i in range(0,number+1,2):
        print(i)

# Example 3

number_list =[]
number = input("Enter a number: ")
while number != "":
    number_list.append(int(number))
    number = input("Enter a number: ")
# print (number_list)
printed =[]
for i in number_list:
    if i > 100 and i not in printed:
        print (i)
        printed.append(i)

# Example 4(
sentence = input("Enter a sentence: ")
sentence = " " + sentence
for i in range(0, len(sentence)):
    if sentence[i] == " " and sentence[i+1] != " ":
        print(sentence[i+1])

