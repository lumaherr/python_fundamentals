'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

#try with a loop
string1 = "hello world"
list1 = string1.split(" ")
print(type(list1))
print(list1)
tuple1 = tuple(list1[0])
tuple2 = tuple(list1[1])
print(type(tuple1))
print(type(tuple2))
list_final = tuple(tuple1) + tuple(tuple2)
list2 = []
list2.append(tuple1)
list2.append(tuple2)
print(list2)
print(type(list2))