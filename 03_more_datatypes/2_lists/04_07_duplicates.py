'''

Write a script that removes all duplicates from a list.

'''

list_dirty = [1, 2, 3, 4, 3, 4, 5]
list_clean = list(set(list_dirty))
print(list_clean)
