a = int(input())
b = input().split(" ")
c = input().split(" ")

d = [int(x) for x in b]
e = [int(x) for x in c]

total = []

for i in range(a):
    total.append(e[i]*((d[i]+d[i+1])/2))
    
print(sum(total))