'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''

#https://stackoverflow.com/questions/1698596/how-can-i-traverse-a-file-system-with-a-generator/1698611#1698611
import os
for root, dirs, files in os.walk('/Users/Lukas/Desktop/jpg_test'):
    for name in files:
        if ".JPG" in name.upper():
            print(name)



'''

import os
thisdir = os.listdir('/Users/Lukas/Desktop/jpg_test')
for each_file in thisdir:
    print(each_file)
    
import glob
os.chdir("/Users/Lukas/Desktop/jpg_test")
list1 = []
for file in glob.glob("*.jpg"):
    list1.append(file)
print(list1)


import os
thisdir = os.listdir('/Users/Lukas/Desktop/jpg_test')
for r, d, f in thisdir:
    for file in f:
        if ".jpg" in file:
            print(os.path.join(r, file))
'''