#unfinished
number = int(input())
count = 0
for x in range(number+1):
    for y in range(number//2 +1):
        if x +y == number:
            count +=1

print(count)