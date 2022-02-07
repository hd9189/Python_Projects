rows = int(input())
cols = rows*2
stars = 1
for x in range((rows//2) +1):
    print("*"*stars + " "*(cols-(stars*2)) + "*"*stars)
    stars +=2

stars -= 2
for x in range(rows//2):
    stars -= 2
    print("*"*stars + " "*(cols-(stars*2)) + "*"*stars)
