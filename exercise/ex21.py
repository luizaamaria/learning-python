'''

user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out a list containing the same items as floats.

The output of your code should be as below:

[10.0, 19.1, 20.0]

'''

# converting the list into a float using the float() function,
# and the map() function will apply this conversion to each element of the list
# The list() function is used to convert the map object into a list of floats

user_entries = ['10', '19.1', '20']
floats = list(map(float, user_entries))
print(floats)

# or

user_entries = ['10', '19.1', '20']
floats = [float(item) for item in user_entries]
print(floats)
