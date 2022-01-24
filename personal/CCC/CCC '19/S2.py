#semi finished
def is_prime(n):
  for y in range(2,n):
    if n%y == 0:
      return False
  return True

a = []
for x in range(int(input())):
  number = int(input())
  down = number
  up = number
  prime = False
  while prime == False:
    if is_prime(up) == True and is_prime(down) == True:
      a.append([up,down])
      prime = True
    else:
      up+=1
      down-=1

for x in a: 
  print(x[0],end = ' ')
  print(x[1])