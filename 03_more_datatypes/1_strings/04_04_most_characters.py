'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
a = input("Write first sentence: ")
b = input("Write second sentence: ")
c = input("Write third sentence: ")

d = len(a)
e = len(b)
f = len(c)

max(d, e, f)
if max(d,e,f) == d:
    print(a)
elif max(d,e,f) == e:
    print(b)
elif max(d,e,f) == f:
    print(c)
else:
    print("Two inputs with same lenght")
