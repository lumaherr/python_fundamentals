'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

numbers_positive = [i for i in numbers if i >= 0]

print(numbers_positive)
