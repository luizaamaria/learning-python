'''

After download the members.txt file, then create a program that, whenever executed,
asks the user to enter a new member in the command line:

Then, the member is added to members.txt. In this case, the text file content would be:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right

'''

member = input("Add a new member: ")

file = open('../files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(member + "\n")

file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()


