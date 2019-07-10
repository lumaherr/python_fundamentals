'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000
input1 = int(input("Write number between 1 and 1000000000: "))

# calls a function that determines whether the number is divisible by both 4 and 7
def divisibility_4_and_7(x):
    if x % 4 == 0 and x % 7 == 0:
        print("True")
    else:
        print("False")

# calls a function that determines whether the number is divisible by 4 or 7
def divisibility_4_or_7(x):
    if x % 4 ==0 or x % 7 == 0:
        print("True")
    else: print("False")

# calls a function that determines whether the number is divisible by 4 and not 7 exclusively
def divisibility_not(x):
    if x % 4 == 0 and x % 7 != 0:
        print("True")
    elif x % 7 == 0 and x % 4 != 0:
        print("True")
    else: print("False")


divisibility_4_and_7(input1)
divisibility_4_or_7(input1)
divisibility_not(input1)

# print the results





# dont know the last bit
"""
if input1 % 4 ==0 or input1 % 7 == 0:
    for i in (range(2,input1-1) if x != 4 and x !=7):
        if input1 % i == 1:
            print("True")
else: print(False)
"""