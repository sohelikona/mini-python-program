import random

def roll_dice():

    dice_drawing = {
        1: (
        " ___________",
        "|           |",
        "|     1     |",
        "|     o     |",
        "|___________|",
        ),
        2: (
        "___________",
        "|  o        |",
        "|     1     |",
        "|        o  |",
        "|___________|",
        ),
         3: (
        "____________",
        "|  o   3    |",
        "|     o     |",
        "|        o  |",
        "|___________|",
        ),
         4: (
        "____________",
        "|  o     o  |",
        "|     4     |",
        "|   o    o  |",
        "|___________|",
        ),
         5: (
        "____________",
        "|  o  5  o  |",
        "|     o     |",
        "|   o    o  |",
        "|___________|",
        ),
        6: (
        "____________",
        "|  o  o  o  |",
        "|     6     |",
        "|  o  o  o  |",
        "|___________|",
        ),
    }


    roll = input("Wanna roll the dice? (Yep/Nope): ")


    while roll.lower() == "Yep".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n.".join(dice_drawing[dice1]))
        print("\n.".join(dice_drawing[dice2]))


        roll = input("Wanna roll again? (Yep/Nope): ")




roll_dice()