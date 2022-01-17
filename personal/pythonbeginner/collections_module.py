#collections: Counter, namedtuple, OrderedDict, defaultdict, deque
'''from collections import Counter
a = "abcabcaaabcaaabbccc"
my_counter = Counter(a)

print(my_counter)
print(my_counter.items)
print(my_counter.keys)
print(my_counter.values)
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())""'''


'''from collections import namedtuple
Point = namedtuple('Point', 'x,y')

pt = Point(1,-4)

print(pt)'''


'''from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['a'] = 1
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)'''


'''from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['c'])'''


from collections import deque

d = deque()

d.append(1)
d.append(3)
d.appendleft(2)
d.append(10)
d.append(29)
d.appendleft(89)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([4,5,7])
print(d)

d.extendleft([55,56,57])
print(d)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)

