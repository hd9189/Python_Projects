import random
options = ["r", "p", "s"]
comp_wins = 0
user_wins = 0

def chooseoptions():
    user_choice = input("Choose Rock, Paper, Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand try again!")
        #runs function
        chooseoptions()
    return user_choice

def computerchoice():
    comp_choice = random.choice(options)
    return comp_choice

#use True to just have a condition
while True:
    #the empty print is just to add a new line
    print("")
    user_choice = chooseoptions()
    comp_choice = computerchoice()
    print("")

    #the first layer of if is for the user, its for each move the user makes
    if user_choice == "r":
        if comp_choice == "r":
            print("You both chose rock! You tied!")

        elif comp_choice == "p":
            print("The computer chose paper! You lose!")
            comp_wins += 1

        #don't always have to end with else in if statement
        elif comp_choice == "s":
            print("The computer chose scissor! You win!")
            user_wins += 1

    elif user_choice == "p":
        if comp_choice == "p":
            print("You both chose paper! You tied!")

        elif comp_choice == "s":
            print("The computer chose scissors! You lose!")
            comp_wins += 1

        # don't always have to end with else in if statement
        elif comp_choice == "r":
            print("The computer chose rock! You win!")
            user_wins += 1

    elif user_choice == "s":
        if comp_choice == "s":
            print("You both chose scissors! You tied!")

        elif comp_choice == "r":
            print("The computer chose rock! You lose!")
            comp_wins += 1

        # don't always have to end with else in if statement
        elif comp_choice == "p":
            print("The computer chose paper! You win!")
            user_wins += 1

    print("")
    print("Player wins: " + str(user_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (Y/N)")
    user_choice.lower()
    if user_choice in ["y", "yes"]:
        pass
    elif user_choice in ["n", "no"]:
        break
    else:
        break