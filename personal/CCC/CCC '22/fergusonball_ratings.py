players = int(input())
stats = [[int(input()), int(input())] for x in range(players)]
gold_players = 0
gold = True
for x in stats:
    if x[0]*5 - x[1]*3 > 40:
        gold_players += 1
    else:
        gold = False

if gold:
    print(f"{gold_players}+")
else:
    print(gold_players)
