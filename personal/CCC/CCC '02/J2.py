words = []
word = input()

while word != "quit!":
    words.append(word)
    word = input()

for w in words:
    if len(w) >=4:
        if w[-2] == "o" and w[-1] == "r" and w[-3] not in "aeiouy":
            word = w[:-2]
            print(word + "our")
        else:
            print(w)
    else:
        print(w)