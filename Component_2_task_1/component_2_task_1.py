

# python 3 program to simulates a Bridge-Keeper.


# Heading printed.
print("Stop! Who would cross the Bridge of Death")
print("Must answer these questions three, 'ere the other side he see.\n")


# Input from user is taken.
name = input("What is your name? \n->")


# Input processed below
if name.upper() == "ARTHUR":
    print("My liege! You may pass!")
else:

    # Input is taken to find the quest.
    quest = input("What is your quest? \n->")

    # Quest processed.
    if "GRAIL" in quest.upper():

        # Colour input is taken to match with the name's first letter.
        colour = input("What is your favourite colour? \n->")

        if(name.lower()[0] == colour.lower()[0]):
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")