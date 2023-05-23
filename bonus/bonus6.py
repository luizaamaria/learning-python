contents = ["Hi",
            "Python",
            "Luiza"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", "w")
    file.write(content)






