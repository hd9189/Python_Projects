limit = int(input())
car = int(input())
if car <= limit: print("Congratulations, you are within the speed limit!")
elif limit < car <= (limit +20): 
    print("You are speeding and your fine is $100.")
elif limit+20 < car <= (limit +30): 
    print("You are speeding and your fine is $270.")
elif (limit +31) <= car: 
    fine = print("You are speeding and your fine is $500.")