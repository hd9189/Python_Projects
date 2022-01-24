#unfinished
row = int(input())
col = int(input())
number = row*col
point = []
grid = []

for x in range(row):
  a = input()
  grid.append(a.split())
  
for x in range(row):
  for y in range(col):
    if int(grid[x][y]) == number:
      point.append((x+1,y+1))