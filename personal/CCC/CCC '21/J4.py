class Section:
    def __init__(self):
        self.l = 0
        self.m = 0
        self.s = 0

#counts book
    def add(self, book):
        if book == "L":
            self.l += 1
        if book == "M":
            self.m += 1
        if book == "S":
            self.s += 1

books = input()
total = Section()
for book in books:
    total.add(book)

#creates seperate section for each book sizes
l = Section()
m = Section()
s = Section()

j = 0
#range of large section
for i in range(total.l):
    l.add(books[j])
    j+=1
for i in range(total.m):
    m.add(books[j])
    j+=1
for i in range(total.s):
    s.add(books[j])
    j+=1

#prints sum of the number of changes, minus the changes made to improve the efficiency
print(l.m+l.s+m.l+m.s - min(m.l, l.m))