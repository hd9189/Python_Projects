
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count <= 0:
        guess = input("Enter Guess: ")
        guess_count += 1
    elif guess_count <= 1:
        print("Hint: it's yellow and brown")
        guess = input("Enter Guess: ")
        guess_count += 1
    elif guess_count <= 2:
        print("Hint: it has a long neck")
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if  out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")