x = int(input())
must_in = [input().split() for y in range(x)]

y = int(input())
must_out = [input().split() for x in range(y)]

g = int(input())
groups = [input().split() for x in range(g)]

violation = 0

for pair in must_in:
    for group in groups:
        if pair[0] in group:
            if pair[1] in group: break
            else:
                violation += 1
                break

for pair in must_out:
    for group in groups:
        if pair[0] in group:
            if pair[1] not in group: break
            else:
                violation += 1
                break

print(violation)