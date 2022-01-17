import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


computer = []

computer_card1 = random.choice(cards)
computer_card2 = random.choice(cards)
comp_total = 0

computer_first = "computers first card is {}".format(computer_card1)
computer.append(computer_card1)
computer.append(computer_card2)

if computer_card1 == "J" or computer_card1 == "Q" or computer_card1 == "K" or computer_card1 == "A":
    comp_val1 = 10
elif computer_card1 != "J" or computer_card1 != "Q" or computer_card1 != "K" or computer_card1 != "A":
    comp_val1 = computer_card1

if computer_card2 == "J" or computer_card2 == "Q" or computer_card2 == "K" or computer_card2 == "A":
    comp_val2 = 10
elif computer_card2 != "J" or computer_card2 != "Q" or computer_card2 != "K" or computer_card2 != "A":
    comp_val2 = computer_card2

comp_total += comp_val1
comp_total += comp_val2

if comp_total < 17:
    computer_card3 = random.choice(cards)
    computer.append(computer_card3)

    if computer_card3 == "J" or computer_card3 == "Q" or computer_card3 == "K" or computer_card3 == "A":
        comp_val3 = 10
    elif computer_card3 != "J" or computer_card3 != "Q" or computer_card3 != "K" or computer_card3 != "A":
        comp_val3 = computer_card3

    comp_total += comp_val3

your_card1 = random.choice(cards)
your_card2 = random.choice(cards)
your_total = 0
yourcards = []
hit = True

yourcards.append(your_card1)
yourcards.append(your_card2)

if your_card1 == "J" or your_card1 == "Q" or your_card1 == "K" or your_card1 == "A":
    your_val1 = 10
elif your_card1 != "J" or your_card1 != "Q" or your_card1 != "K" or your_card1 != "A":
    your_val1 = your_card1

if your_card2 == "J" or your_card2 == "Q" or your_card2 == "K" or your_card2 == "A":
    your_val2 = 10
elif your_card2 != "J" or your_card2 != "Q" or your_card2 != "K" or your_card2 != "A":
    your_val2 = your_card2

your_total += your_val1
your_total += your_val2

first_cards = "Your cards are {} and {}. Your total is {}".format(your_card1, your_card2, your_total)

while hit:
    print(first_cards)
    choice1 = input("Would you like to hit or stand?: ")
    choice1 = choice1.upper()

    if choice1 == "HIT":
        your_new_card = random.choice(cards)
        yourcards.append(your_new_card)

        if your_new_card == "J" or your_new_card == "Q" or your_new_card == "K" or your_new_card == "A":
            your_new_card_val = 10
        elif your_new_card != "J" or your_new_card != "Q" or your_new_card != "K" or your_new_card != "A":
            your_new_card_val = your_new_card

        your_total += your_new_card_val
        first_cards = ("Your new card is {}. Your total is {}".format(your_new_card, your_total))
        print(first_cards)
        hit = False


    else:
        hit = False

if your_total > 21:
    print("You went bust!")
    print("You Lose!")

elif comp_total > 21 and your_total < 21:
    print("Computer went bust!")
    print("Computer drew:" + str(computer))
    print("You win!")

elif comp_total < 21 and your_total < 21 and comp_total == your_total:
    print("You tied!")
    print("You and the computer got: " + str(your_total))

elif comp_total < 21 and your_total < 21 and comp_total < your_total:
    print("Computer drew: " + str(computer))
    print("It's total was: " + str(comp_total))
    print("You win!")

elif comp_total < 21 and your_total < 21 and comp_total > your_total:
    print("Computer drew: " + str(computer))
    print("It's total was: " + str(comp_total))
    print("You Lose!")
