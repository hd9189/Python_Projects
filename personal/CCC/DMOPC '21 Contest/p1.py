d = int(input())
number = list(input())
for x in range(1,d):
    if int(number[x-1])< int(number[x]):
        numbers = number[x-1]
        number[x-1] = number[x]
        number[x] = numbers
        break

number = ''.join(number)
print(int(number))