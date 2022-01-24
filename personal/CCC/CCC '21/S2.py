rows = int(input())
cols = int(input())
canvas = []
for x in range(rows):
  canvas.append(["B" for y in range(cols)])


def change_row(row):
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
    
print(sum([x.count("G") for x in canvas]))