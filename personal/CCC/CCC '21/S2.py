rows = int(input())
cols = int(input())
canvas = []
for x in range(rows):
  canvas.append([0 for y in range(cols)])

changes = int(input())

l_change = [input().split() for x in range(changes)]

for paint in l_change:
  if paint[0] == "R":
    for x in range(len(canvas[0])):
      canvas[int(paint[1])-1][x] +=1

  elif paint[0] == "C":
    for x in range(len(canvas)):
      canvas[x][int(paint[1]) -1] +=1
  
count = 0

for x in range(len(canvas)):
  for y in range(len(canvas[0])):
    if canvas[x][y] %2 == 1:
      count +=1

print(count)


'''def change_row(row):
  for x in range(len(canvas[row -1])):
    if canvas[row][x] == "B":
      canvas[row][x] = "G"
    elif canvas[row][x] == "G":
      canvas[row][x] = "B"
            
def change_col(col):
  for x in range(len(canvas)):
    if canvas[x][col] == "B":
      canvas[x][col] = "G"
    elif canvas[x][col] == "G":
      canvas[x][col] = "B"


for i in range(int(input())):
  change = input().split()
  if change[0] == "R":
    change_row(int(change[1])-1)
  elif change[0] == "C":
    change_col(int(change[1])-1)
    
print(sum([x.count("G") for x in canvas]))'''