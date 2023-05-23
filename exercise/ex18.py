'''

Then, create a program that reads each text file and prints out the content of each in the command line.

'''

filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    content = file.read()
    print(content)
