'''

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

3. Prints out the amount in euros, as shown in the screenshot below.

    how many dollars have you got? 100
    The amount in euros is:
    95.0

'''
value = 0.95


dollar = float(input("How many dollars have you got? "))
euro = dollar * value

print(f"The amount in euros is: {euro}")
# print(euro)
