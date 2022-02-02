n = int(input())
k = int(input())
a = [n]
num = n
for x in range(k):
    num*=10
    a.append(num)

print(sum(a))

