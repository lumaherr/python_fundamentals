'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input: 1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
input1 = []
for i in range(0,10) :
    number = int(input("Please type a number: "))
    input1.append(number)
print("Initial List: ", input1)

list1 = []
for i in [1,3,5,7,9]:
        list1.append(input1[i])
list2 = []
for i in [8,6,4,2,0]:
    list2.append(input1[i])

print(list1)
print(list2)