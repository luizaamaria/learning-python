'''

Create a program that prompts the user to input their name repeatedly.
Then, the program repeatedly prints out the name with the first letter capitalized.

'''

prompt = "What's your name? "
names = []

while True:
    name = input(prompt)
    print(name.capitalize())
    names.append(name)
    print(names)

################################

# while True:
#     name = input("What's your name? ")
#     print(name.capitalize())
#     print(name)
