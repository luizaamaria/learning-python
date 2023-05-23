'''

Create a program that generates multiple text files by iterating over the filenames list.
The text Hello should be written inside each generated text file.

'''

# content = ["Chocolate", "Brigadeiro", "Doce"]
#
# filename = ["doc.txt", "doc1.txt", "doc2.txt"]
#
# for content, filename in zip(content, filename):
#     file = open(f"../files/{filename}", "w")
#     file.write(content + "\nHello")

# or

filenames = ["doc.txt", "doc1.txt", "doc2.txt"]

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
