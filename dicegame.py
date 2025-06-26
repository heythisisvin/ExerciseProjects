import random

while True:
    #ask the user to roll the dice and all answer in lower case
    roll_dice = input("Roll the dice? (y/n): ").lower()
    #y will play the game, n will quit and others will ask to select again.

    #generate number using random.int from 1 to 6
    #create 2 for dice 1 and dice 2
    random_roll1 = random.randint(1, 6)
    random_roll2 = random.randint(1, 6)

    #create condition  for the answer
    #continue means if invalid will run the loop again.
    if roll_dice != "y" and roll_dice != "n":
        print("Invalid input. Please try again.")
        continue
    #break means it stopp the loop and exit.
    if roll_dice == "n":
        break
    #else pag nag y print niya yung roll 1 and roll 2 na random.
    else:
        print(random_roll1, random_roll2)

print("Thank you for playing!")


