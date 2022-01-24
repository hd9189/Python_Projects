grid = [[1,2],[3,4]]
a = [x for x in input()]

def horizontal(g):
  a = g[0]
  g[0] = g[1]
  g[1] = a
  grid = g

def vertical(g):
  a = g[0][0]
  b = g[1][0]
  g[0][0] = g[0][1]
  g[1][0] = g[1][1]
  g[0][1] = a
  g[1][1] = b
  grid = g

for y in a:
  if y == "H":
    horizontal(grid)
  elif y == "V":
    vertical(grid)

for z in grid:
  print(z[0], end =' ')
  print(z[1])