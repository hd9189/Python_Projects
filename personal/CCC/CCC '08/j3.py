pad = [['A','B','C','D','E','F'],['G','H','I','J','K','L'],['M','N','O','P','Q','R'],['S','T','U','V','W','X'],['Y','Z',' ','-','.','enter']]
string = input()
moves = 0
current = [0,0]
next = [0,0]
for letter in string:
    for row in pad:
        if letter in row:
            moves += (abs(current[1]-next[1]))
            next[0] = row.index(letter)
            moves += (abs(current[0]-next[0]))
            current = next
        else:
            next[1] +=1
    print(moves)
        
moves += (5-current[0])+ (4-current[1])
print(moves)