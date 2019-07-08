'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

a = "Hello friend, How are you !"
print("Initial sentence: " + a)
print("")
b = a.replace("H", "$")
print("Changed sentence: " + b)