'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
string1 = "hello world"
list1 = string1.split(" ")
print(type(list1))
print(list1)
tuple1 = tuple(list1[0])
tuple2 = tuple(list1[1])
print(type(tuple1))
print(tuple1)
print(type(tuple2))
print(tuple2)
list_final = tuple(tuple1) + tuple(tuple2)

print(list_final)
print(type(list_final))


#i can just do a tuple with 2 lists but not the other way around