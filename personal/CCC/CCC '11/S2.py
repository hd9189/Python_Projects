number = int(input())

a = [input() for x in range(number)]
ak = [input() for x in range(number)]
right = 0
for x in range(number):
  if a[x] == ak[x]:
    right +=1
print(right)