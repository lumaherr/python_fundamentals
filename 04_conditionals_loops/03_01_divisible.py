'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
input1 = int(input("Type a number between 1 and 1000000000: "))
if input1 % 3 == 0 :
    print("Yeees its divisible by 3:", input1/3)
else :
    print("Sorry, your number is not divisble by 3")
