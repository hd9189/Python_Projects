choice = int(input())
num = int(input())
a = input().split()
b = input().split()
a = [int(x) for x in a]
b = [int(x) for x in b]
c = []

if choice == 1:
  a.sort()
  b.sort()
  for x in range(num):
    c.append(max(a[x],b[x]))
  print(sum(c))

elif choice == 2:
  a.sort()
  b.sort(reverse=True)
  for x in range(num):
    c.append(max(a[x],b[x]))
  print(sum(c))