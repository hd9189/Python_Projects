'''available = 10
c = 0
candies = float(input("How many candies do you want? : "))

while c <= candies:

    if c > available:
        print("No more candies :(")
        break

    print("You got a candy!")
    c += 1'''

'''for i in range(1,101):
    if i%3==0 or i%5==0:
        continue

    print(i)

print("done")'''

for i in range(1,101):
    if (i%2 != 0):
        pass

    else:
        print(i)