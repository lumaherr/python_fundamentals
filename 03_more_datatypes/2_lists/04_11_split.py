'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
a = input("Write a sentence: ")
b = a.split()
print(b)

from statistics import mode #modus zeigt an, welches item am öftesten vorhanden ist
def most_common(b):
    return mode(b)
print(most_common(b))