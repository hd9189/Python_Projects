winner = ""
big = 0
for x in range(int(input())):
    person = input()
    amount = int(input())
    if amount > big:
        big = amount
        winner = person

print(winner)

