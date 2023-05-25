'''

user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out the sum of the numbers.

The output of your code should be as below:

49.1
Hint: Use the sum() function. The function gets a list of numbers
as input and produces the sum of all numbers. For more info, try help(sum).

'''

user_entries = ['10', '19.1', '20']

floats = [float(item) for item in user_entries]
print(sum(floats))
