'''

filenames = ['document', 'report', 'presentation']

Copy-paste the above list in a .py file and extend the code, so it prints out the output below:

0-Document.txt
1-Report.txt
2-Presentation.txt


'''

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")

