'''
Code a game of rock paper scissors.

'''


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass


# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    pass


'''
Start here

'''

input_user = int(input("Type in a number between 0 and 2 (0 = scissor, 1 = rock, 2 = paper): "))

import random

input_mac = random.randint(0, 2)

# i dont know how to write this correct

def get_hand(n):
    if n == 0:
        print("scissor")
    elif n == 1:
        print("rock")
    elif n == 2:
        print("paper")
    else:
        print("error, user typed in not wanted number")
    return get_hand()


a = get_hand(input_user)
b = get_hand(input_mac)
print(a)
print(b)

if a == b:
    print("You tied!")
elif a == "scissor":
    if b == "rock":
        print("You lost :(")
elif a == "rock":
    if b == "scissor":
        print("You won!")
elif a == "paper":
    if b == "rock":
        print("You won!")
elif a == "rock":
    if b == "paper":
        print("You lost :(")
elif a == "scissor":
    if b == "paper":
        print("You won!")
elif a == "paper":
    if b == "scissor":
        print("You lost :(")



# take in a number 0-2 from the user that represents their hand

# generate a random number 0-2 to use for the computer's hand

# call the function get_hand to get the string representation of the user's hand

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out the winner

# print out the player hand and computer hand

# print out the winner
