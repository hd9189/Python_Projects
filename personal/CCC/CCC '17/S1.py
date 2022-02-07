days = int(input())
swifts = [int(x) for x in input().split()]
semaphores = [int(x) for x in input().split()]
k = 0
sw = 0
sem = 0
for day in range(days):
    sw += swifts[day]
    sem += semaphores[day]
    if sw == sem:
        k = day+1

print(k)
