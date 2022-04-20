string = list(input())
set = set(string)
value = []
for x in set:
    value.append(string.count(x))
for x in range(2):
    if len(value) != 0:
        value.remove(max(value))
print(sum(value))