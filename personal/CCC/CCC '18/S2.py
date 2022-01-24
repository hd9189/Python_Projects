
a = int(input())
c = []

for x in range(a):
  b = input().split()
  c.append(b)

#find the smallest number in 4 corners
corner = [c[0][0], c[0][-1],c[-1][0],c[-1][-1]]
corner = [int(x) for x in corner]
small_index = corner.index(min(corner))

#top left
if small_index == 0:
  for x in c:
    for y in x:
      print(y, end = " ")
    print('')
#top right corner, flip -90 degrees
elif small_index == 1:
  for y in range(a,0,-1):
    for x in c:
      print(x[y-1], end = " ")
    print()
elif small_index == 3:
  for x in range(a, 0, -1):
    for y in range(a, 0, -1):
      print(c[x-1][y-1], end = " ")
    print()
elif small_index == 2:
  for y in range(a):
    for x in range(a,0,-1):
      print(c[x-1][y], end = " ")
    print()