times = int(input())
yesterday = input()
today = input()
count = 0
for x in range(times):
    if yesterday[x] == "C" and today[x] == "C": count += 1

print(count)