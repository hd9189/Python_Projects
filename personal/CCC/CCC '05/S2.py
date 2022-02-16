size = input().split()
width = int(size[0])
height = int(size[1])

position = [0,0]
places = []

while True:
    move = input()
    if move == "0 0":
        break
    else:
        move = move.split()
        move = [int(x) for x in move]
        position[0] += move[0]
        position[1] += move[1]
        if position[0] < 0:
            position[0] = 0
        elif position[0] > width:
            position[0] = width
        if position[1] < 0:
            position[1] = 0
        elif position[1] > height:
            position[1] = height
        places.append([position[0], position[1]])

for x in places:
    print(x[0], x[1])


