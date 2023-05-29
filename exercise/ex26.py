"""

Build a percentage calculator that gets from the user the "total value"
and the "value" and returns the percentage.


The program should also print a message if the user doesn't
 enter a number for the "total value or for the "value

"""
try:
    value = float(input("Enter total value: "))
    value_part = float(input("Enter value: "))

    porcentage = (value_part / value ) * 100

    print(f"That is {porcentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")
