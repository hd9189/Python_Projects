numbers = [1,2,3,5]

#print all metholds and functions of an object
print(dir(numbers))

#prints iterator object and the location of this object
value = numbers.__iter__()
print(value)

item_1 = value.__next__()
print(item_1)

item_2 = value.__next__()
print(item_2)

item_3 = value.__next__()
print(item_3)

values_better = iter(numbers)
print(values_better)

#simpler and python way of doing it
item_4 = next(values_better)
item_5 = next(values_better)
item_6 = next(values_better)

print(item_4, item_5, item_6)

#class to print even numbers
class Even:
    #everything beside self is something the user provides
    def __init__(self, max):
        #first value is always 2, because its the lowest even number
        self.n = 2
        #value that we provide
        self.max = max

    def __iter__(self):
        #iter must implement an item method which return an iterator
        return self

    def __next__(self):
        if self.n <= self.max:
            #first return the smaller value
            result = self.n
            #then increase value of n
            self.n += 2
            return result

        else:
            raise StopIteration

num = Even(12)
print(next(num), next(num), next(num), next(num))

