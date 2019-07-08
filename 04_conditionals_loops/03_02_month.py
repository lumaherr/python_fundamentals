'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
input1 = int(input("Write an integer: "))
if 0<input1<13 :
    if input1 == 1:
        print("January")
    elif input1 == 2:
        print("February")
    elif input1 == 3:
        print("March")
    elif input1 == 4:
        print("April")
    elif input1 == 5:
        print("May")
    elif input1 == 6:
        print("June")
    elif input1 == 7:
        print("July")
    elif input1 == 8:
        print("August")
    elif input1 == 9:
        print("September")
    elif input1 == 10:
        print("October")
    elif input1 == 11:
        print("November")
    elif input1 == 12:
        print("December")
else:
    print("other")