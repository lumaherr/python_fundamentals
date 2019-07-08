'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''

input1 = int(input("Type a lower bound number: "))
input2 = int(input("Type a upper bound number: "))
sum = 0
for i in range(input1, input2+1):
    sum += i
print("The sum is: ", sum)