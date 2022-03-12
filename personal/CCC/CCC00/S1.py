quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

count = 1
turns = 0

while quarters > 0:
    if count == 1:
        first += 1
        if first == 35:
            first = 0
            quarters += 30

    elif count == 2:
        second += 1
        if second == 100:
            second = 0
            quarters += 60

    elif count == 3:
        third += 1
        if third == 10:
            third = 0
            quarters += 9

    turns += 1
    count += 1
    quarters -= 1
    if count == 4:
        count = 1

print(f"Martha plays {turns} times before going broke.")