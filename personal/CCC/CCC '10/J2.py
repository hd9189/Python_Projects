a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

whole_n = (s//(a+b))*(a-b)
whole_b = (s//(c+d))*(c-d)

nikky = s%(a+b)
byron = s%(c+d)

for i in range(nikky):
    if i < a:
        whole_n += 1
    elif i >= a:
        whole_n -= 1

for i in range(byron):
    if i < c:
        whole_b += 1
    elif i >= c:
        whole_b -= 1

if whole_n == whole_b:
    print("Tied")
elif whole_n > whole_b:
    print("Nikky")
elif whole_n < whole_b:
    print("Byron")