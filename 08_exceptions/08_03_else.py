'''
Write a script that demonstrates a try/except/else.

'''

try:

    a = int(input("Type a number here: "))
    b = int(input("Type a second number: "))
    print(a / b)

except ValueError:
    print("No other values than numbers are allowed")
except ZeroDivisionError:
    print("No zeros allowed")
else:
    print(a*b)