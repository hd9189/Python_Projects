n = int(input())
l = list(map(int, input().split()))

for x in range(1,n+1):
    if x in l:
        l.remove(x)
    else:
        print(x)
        break