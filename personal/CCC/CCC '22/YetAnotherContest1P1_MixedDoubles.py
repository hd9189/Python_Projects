#giveup

a = input().split()
a = [int(x) for x in a]
men = input().split()
men = [int(man) for man in men]
women = input().split()
women = [int(woman) for woman in women]
men.sort()
women.sort()
small_half = a[1]//2
big_half = a[1] - small_half
if men[-1] >= women[-1]:
    men[-1] += big_half
    women[-1]+= small_half
elif women[-1] > men[-1]:
    women[-1]+= big_half
    men[-1]+= small_half
    
count = 0
for x in range(a[0]):
    count += men[x] * women[x]
