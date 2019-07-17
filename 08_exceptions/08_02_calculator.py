'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    a = int(input("Type a number here: "))
    b = int(input("Type a second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Second number can't be zero")
except ValueError:
    print("No other values than numbers are allowed")
