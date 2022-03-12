number = int(input()); ways = 0
#divised by 4 because if all 4s it can do it
for x in range((number//4)+1): 
    # if x*4 is number then it will still equal 0, and when x is 0, it will check all 5's
    if (number-(x*4))%5 == 0: ways += 1
print(ways)