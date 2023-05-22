'''

Here is another piece of code that contains a bug:

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print("f{i}.{j}")
The expected output is this:

0.pasta
1.pizza
2.salad
Fix the bug so the program prints out the above output.

'''

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")

