number = [int(input()) for x in range(4)]

def Fish_At_Constant_Depth():
    for x in range(1,len(number)):
        if number[x] != number[x-1]:
            return "No Fish"

    return "Fish At Constant Depth"

def Fish_Rising():
    for x in range(1,len(number)):
        if number[x] <= number[x-1]:
            return "No Fish"
    
    return "Fish Rising"

def Fish_Diving():
    for x in range(1,len(number)):
        if number[x] >= number[x-1]:
            return "No Fish"
    
    return "Fish Diving"

if number[1] == number[0]:
    print(Fish_At_Constant_Depth())
elif number[1] > number[0]:
    print(Fish_Rising())
elif number[1] < number[0]:
    print(Fish_Diving())