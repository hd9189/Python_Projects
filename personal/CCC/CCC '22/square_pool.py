def max_square(MATRIX):
    row = len(MATRIX)
    col = len(MATRIX[0])
 
    S = []
    for i in range(row):
      temp = []
      for j in range(col):
        if i==0 or j==0:
          temp += MATRIX[i][j],
        else:
          temp += 0,
      S += temp,

    for i in range(1, row):
        for j in range(1, col):
            if (MATRIX[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(row):
        for j in range(col):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
 
    count = 0
    for i in range(max_i, max_i - max_of_s, -1):
        count += 1
    print(count)

n = int(input())
t = int(input())
coordinates = [list(map(int, input().split())) for x in range(t)]

graph = [[1 for x in range(n)] for y in range(n)]

for x in coordinates:
    graph[x[0]-1][x[1]-1] = 0

max_square(graph)