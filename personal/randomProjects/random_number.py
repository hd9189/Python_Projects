import random

def guess_num():
    secret = random.randint(1, max)
    tries = 0
    while tries >= 0:
        answer = input("Guess a number from 1 to " + str(max) + ": ")
        answer = int(answer)
        if answer == secret:
            tries += 1
            print("Congrats! You got it right!")
            # return abruptly stops a loop
            return("Number of tries: " + str(tries))

        else:
            print("wrong Number try again!")
            tries += 1

flag = True

while flag:
    #input is in while loop to enter new number when it's wrong
    max = input("Type a number for an upper bound: ")
    #use is.digit because the answer is still a string
    if max.isdigit():
        print("Let's play!")
        #turns the string answer to a number
        max = int(max)
        #helps get out of while loop
        flag = False
    else:
        print("Not a number! Try Again!")
        #theres not flag = False because it would break out of the loop
print(guess_num())



