'''
Demonstrate the use of the .enumerate() function.
'''

my_list = ["hi", "my", "name", "is", "Lukas", "and", "I am", "22", "years", "old" ]

for i, c in enumerate(my_list, 1):
    print(f"The word: {c}, is number: {i} in the list ")