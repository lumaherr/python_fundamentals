'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
a = input("Please type a Sentence here: ")
print(*map(a.lower().count, "aeiou"))

