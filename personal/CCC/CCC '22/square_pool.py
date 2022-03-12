def max_square(MATRIX):
    row = len(MATRIX)
    col = len(MATRIX[0])
 
    #put 1 to the top and left side, because they can't go and create a square as the bottom left corner, and don't have a tree, if have then it becomes 0 as well
    copy_matrix = []
    for x in range(row):
      temporary = []
      for y in range(col):
        if x==0 or y==0:
          temporary += MATRIX[x][y],
        else: temporary += 0,
      copy_matrix += temporary,
    #add 1 to the minimum of all the rest top, top left, and left boxes if the box is not a tree, then puts the new value in other matrix
    for x in range(1, row):
        for y in range(1, col):
            if (MATRIX[x][y] == 1):
                copy_matrix[x][y] = min(copy_matrix[x][y-1], copy_matrix[x-1][y], copy_matrix[x-1][y-1]) + 1
            #if not 1 then it will be 0 in the matrix cuz its all ones and zeros
            else:
                copy_matrix[x][y] = 0
    #find the index of the largest value in other matrix
    max_of_copy_matrix = copy_matrix[0][0]
    max_x = 0
    max_y = 0
    for x in range(row):
        for y in range(col):
            if (max_of_copy_matrix < copy_matrix[x][y]):
                max_of_copy_matrix = copy_matrix[x][y]
                #only need to find either just x or y value, cuz its a square, and finding the max value of the s value is enought o determine if its larger
                max_x = x
 #print number using for loop, because I only have indexes
    count = 0
    for i in range(max_x, max_x - max_of_copy_matrix):
        count += 1
    print(count)

n = int(input())
t = int(input())
coordinates = [list(map(int, input().split())) for x in range(t)]

graph = [[1 for x in range(n)] for y in range(n)]

for x in coordinates:
    graph[x[0]-1][x[1]-1] = 0

max_square(graph)