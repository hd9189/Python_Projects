def count(string):
    for letter in string:
        if string.count(letter) > 1:
            return False
    
    return True
input = int(input())
a = input+1
while True:
    y = count(str(a))
    if y:
        print(a)
        break
    else:
        a+=1


