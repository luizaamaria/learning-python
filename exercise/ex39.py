'''


Define a function that converts fluid ounces to milliliters knowing that 1
fluid ounce is equal to 29.57353 milliliters. For example, I was to call your function with foo(1)
I would get an output of 29.57353. If I called it with  foo(5) I would get 147.86765, and so on.

'''

def converts(n):
    build = 29.57353
    result = build * n

    return result

print(converts(5))

# or

def foo(oz):
    # Multiply the input value (oz) by the conversion factor 29.57353
    return oz * 29.57353