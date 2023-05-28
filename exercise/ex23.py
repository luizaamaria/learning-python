"""

A client wants to buy a coin-flip probability program from you.

The programs should work like this:

1. The user runs the program. The program asks the user to enter "head" or "tail".
The user flips a coin on their desk, table, floor, etc.,
and then enters "head" or "tail". The user does the same over and over again.

In each cycle, the program should return the current percentage of heads in the program,
similar to what you see in the screenshot above. Also, you should write each user entry
(i.e., head or tail) in a text file using a with-context manager, one entry per line

"""

while True:
    with open("../files/sides.txt", 'r') as file:  # open the file in read mode
        sides = file.readlines()  # Reads the lines from the file and stores the values in a list

    side = input("Throw the coin and enter head or tail here: ") + "\n"

    sides.append(side)  # Adds the side variable to the sides list

    with open("../files/sides.txt", 'w') as file:  # open the file in write mode
        file.writelines(sides)  # Writes the contents of the sides list to the file

    nr_heads = sides.count("head\n")  # Counts the number of occurrences of the string "head\n" in the sides list.
    percentage = nr_heads / len(sides) * 100  # Calculates the percentage of "head" in relation to total launches.
    # Divide the number of "head" by the length of the sides list and multiply by 100.

    print(f"Heads: {percentage}%")
