people = int(input())
peoples = []
number = []
num = people//2 +1
for person in range(people):
    info = input().split()
    peoples.append([info[0], int(info[1])])
    number.append(int(info[1]))
number.sort()
for person in range(len(peoples)):
    if number.index(peoples[person][1]) >= num:
        print(f"{peoples[person][0]} is cute! <3")
    else:
        print(f"{peoples[person][0]} is not cute. </3")
