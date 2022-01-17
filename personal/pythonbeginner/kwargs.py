def person1(name, *data):
    print(name)
    print(data)

person1('navin', 28, 'Mumbai', 9865432)

def person2(name, **data):
    print(name)
    print(data)
print("")
person2('navin', age=28, city='Mumbai', mob=9865432)

def person3(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)
print("")
person3('navin', age=28, city='Mumbai', mob=9865432)
