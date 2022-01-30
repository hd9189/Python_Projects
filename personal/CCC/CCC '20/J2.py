p = int(input())
n = int(input())
r = int(input())

infected = n
people = n
day = 0

while True:
    people = people + (infected*r)
    infected = infected*r
    day += 1
    if people >= p:
        if people == p:
            print(day+1)
        else:
            print(day)
        break