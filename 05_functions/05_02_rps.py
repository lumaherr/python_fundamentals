'''
Code a game of rock paper scissors.

'''


# function to get hand based on number

# the function should take in a number and return the string representation of the hand

    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"



# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
while True:

    input_user = int(input("Type in a number between 0 and 2 (0 = scissor, 1 = rock, 2 = paper): "))

    import random

    input_mac = random.randint(0, 2)

    # i dont know how to write this correct

    def get_hand(n):
        if n == 0:
            return "scissor"
        elif n == 1:
            return "rock"
        elif n == 2:
            return "paper"
        else:
            return "Type a number between 0 and 2"

    a = get_hand(input_user)
    b = get_hand(input_mac)
    print(a)
    print(b)

    if a == b:
        print("You tied!")


    if a == b:
        print("You tied!")
    elif a == "scissor":
        if b == "rock":
            print("You lost :(")
        elif b == "paper":
            print("You won!")
    elif a == "rock":
        if b == "scissor":
            print("You won!")
        elif b == "paper":
            print("You lost :(")
    elif a == "paper":
        if b == "rock":
            print("You won!")
        elif b == "scissor":
            print("You lost :(")


