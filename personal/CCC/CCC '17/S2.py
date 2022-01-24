a = int(input())
b = [int(x) for x in input().split()]
b.sort()
d = []
r = 0

if a %2  == 0:
  for x in range(a//2):
    c = (a//2) -1
    d.append(b[c-r])
    d.append(b[c+r+1])
    r +=1

elif a %2 !=0:
  r = 0
  c = a//2
  for x in range(c):
    d.append(b[c-r])
    d.append(b[c+r+1])
    r+=1
  d.append(b[0])

for x in d:
  print(x, end = " ")