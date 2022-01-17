class Point():
    def __init__(self, x= 0, y=0):
        self.x =x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    #p is the second coordinate, self is the first
    #to use these functions just use + - * like normal, this is just to set what it means

    # add +
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    #subtract -
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    #multiply *
    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y)

    #get single value of length of a point to (0,0)
    def length(self):
        import math
        #square root
        return math.sqrt(self.x**2 + self.y**2)

    #now it is comparisions like < > <= >= ==

    #greater than >
    #self and p are the self in the length function
    def __gt__(self, p):
        #return if True, return False if false
        return self.length() > p.length()

    #greater than or equal to >=
    def __ge__(self, p):
        return self.length() >= p.length()

    #less than <
    def __lt__(self, p):
        return self.length() < p.length()

    #less than or equal to <=
    def __le__(self, p):
        return self.length() <= p.length()

    #equal to ==
    #because sometimes the length will return decimal numebers so it can't be exactly equal
    def __eq__(self, p):
        return self.x == p.x and self.y ==p.y


    #turns the result into a string, because if it was just a number it would return the adress instead.
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p5 = p1 +p2
p6 = p3 -p4
p7 = p1 * p3
print(p5,p6,p7)

print(p1 == p2)
print(p3 < p1)
print(p4 >= p2)
print(p3 == p4)