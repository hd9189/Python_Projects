a = [int(x) for x in input().split()]
t = input()
speed = a[1]
count = 0
for x in range(a[0]):
    if t[x] == "U" and speed >0: speed -=1
    elif t[x] == "D": speed +=1
    if speed == 0: count +=1
print(count)