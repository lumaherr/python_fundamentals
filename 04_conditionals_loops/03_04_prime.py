'''
Print out every prime number between 1 and 100.

'''
lower_border = int(1)
upper_border = int(100)

print("Prime numbers between:", lower_border, "and", upper_border, "are: ")
for num in range(lower_border,upper_border):
    if num >1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)