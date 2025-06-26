import random

user_score = 0
computer_score = 0

Options = ['bato', 'papel', 'gunting']
#bato : 0, papel :1, gunting : 2
#assigment para sa random

while True:
    play_input = input("Play Batobatopik. bato/papel/gunting? (type q to quit): ").lower()
    if play_input == 'q':
        break

    if play_input not in Options:
        print("Invalid input. Please try again.")
        continue

    random_number = random.randint(0, 2)
    #ito nag assign ng range para sa random number

    random_option = Options[random_number]
    #ito ginamit yung result ng random number para makuha output sa options list
    #using the indexing Options[0] or 1 or 2. and dito na rin assignment ng bato
    #papel at gunting.

    if play_input == 'bato' and random_option == 'gunting':
         print("You win!")
         user_score += 1

    elif play_input == 'papel' and random_option == 'bato':
        print("You win!")
        user_score += 1

    elif play_input == 'gunting' and random_option == 'papel':
        print("You win!")
        user_score +=1
    else:
        print("You lose!")
        computer_score += 1

print(f"You won {user_score} times.")
print(f"Computer won {computer_score} times")
print(f"Goodbye!")