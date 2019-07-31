'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

for i in famous_quotes:
    name = i["full_name"]
    name_list = name.split(" ")
    first_name = name_list[0]
    last_name = name_list[-1]
    quote = i["quote"]
    print(f"\"{quote}\" - {last_name}, {first_name}")

#loop through famous quote list:
    #set current dictionaries quote = to current quote variable
    #set full name = to full name variable
    #split full name variable into 2
    #take this when printing out the string print("quote", last name, first name"


#'(f"{last name} first name)

'''
print(famous_quotes.values())

print(famous_quotes[])
#no clue
'''

