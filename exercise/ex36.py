'''

As you can see, the program first asks the user to enter a whole number.
Then, once the user enters a number, the program asks the user again to enter another number.

Then, the program returns a random number that falls between the two whole numbers.


'''
from random import randint, random

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

rand = randint(lower, upper)
# or using the function randrange
print(rand)









