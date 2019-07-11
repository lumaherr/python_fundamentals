'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
user_input = input("Type a word: ")
user_input_list = list(user_input)

from collections import Counter
cc = Counter(user_input_list)
dict1 = dict(cc)

print(dict1)
