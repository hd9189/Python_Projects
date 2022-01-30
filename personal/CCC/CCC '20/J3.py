dots = int(input())
points = []
h_large = 0
h_small = 101
v_large = 0
v_small = 101
for x in range(dots):
    points.append(input().split(","))

for y in points:
    if int(y[0]) <= h_small: h_small = int(y[0])-1
    if int(y[0]) >= h_large: h_large = int(y[0])+1
    if int(y[1]) <= v_small: v_small = int(y[1])-1
    if int(y[1]) >= v_large: v_large = int(y[1])+1

print(h_small, end = ",")
print(v_small)
print(h_large,end = ",")
print(v_large)
