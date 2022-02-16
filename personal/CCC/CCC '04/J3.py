num_adj = int(input())
num_noun = int(input())
adj = [input() for x in range(num_adj)]
noun = [input() for x in range(num_noun)]

for word in adj:
    for object in noun:
        print(f"{word} as {object}")
