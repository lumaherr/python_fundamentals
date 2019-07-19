'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
gen = (i for i in range(1,500) if i%3 == 0 and i%5 != 0)

for i in gen:
    print(i)