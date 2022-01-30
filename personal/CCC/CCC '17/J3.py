start = tuple(int(x) for x in input().split(" "))
end = tuple(int(x) for x in input().split(" "))
battery = int(input())
a, b = start
c, d = end
x = abs(a-c)
y = abs(b-d)
if (battery - (x+y))%2 == 0 and battery >= (x+y):
    print("Y")
else:
    print("N")