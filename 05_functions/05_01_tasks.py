'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

input1 = int(input("Write number between 1 and 1000000000: "))
if input1 % 4 == 0 and input1 % 7 == 0:
    print("True")
else: print(False)
if input1 % 4 ==0 or input1 % 7 == 0:
    print("True")
else: print(False)


# dont know the last bit
"""
if input1 % 4 ==0 or input1 % 7 == 0:
    for i in (range(2,input1-1) if x != 4 and x !=7):
        if input1 % i == 1:
            print("True")
else: print(False)
"""