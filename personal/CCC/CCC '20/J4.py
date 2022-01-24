t = input()
a = input()
update = []
c = a


for x in range(len(a)):
  update.append(c)
  b = list(c)
  b.append(b[0])
  b.pop(0)
  c = "".join(b)

for i in range(len(update)):
  if update[i] in t:
    print("yes")
    break
  elif i + 1 == len(update):
    print("no")

