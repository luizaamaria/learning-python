'''

Write a get_nr_items function that:

1. gets one parameter. The parameter is expected to be a list of strings.

2. returns the number of items the list contains.

'''


def get_nr_items(user_input):
    items = user_input.split(',')

    return len(items)





