thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#key doesn 't exist so theres key error
x = thisdict["model"]
print(x)#.get just prints None, so it doesn 't break the code
print(thisdict.get("model"))

if "model" in thisdict:
    print("yes, model is in the car_dict dictionary")

dict = {
    'hello': 'world'
}
print(dict.get('hello', 'default_val'))# prints the 2n d variable
#if the key doesn 't exist
print(dict.get('thing', 'default_val'))
print(dict.get('thing', None))

# Dictionary - Add
thisdict["color"] = "red"
thisdict['year'] = 2020
print(thisdict)

# Dictionary - Remove
thisdict.pop("model")
del thisdict["brand"]
print(thisdict)

thisdict['model'] = 'ABC'
thisdict["brand"] = 'Ferarri'

# iterate through the dicitonary
for x in thisdict:
    print(x)
print(thisdict[x])
print("key: {}, Value: {}".format(x, thisdict[x]))

for y in thisdict.values():
    print(y)

for x, y in thisdict.items():
    print(x, y)

# points towards dictionary
new_car_dict = thisdict# creates actual dictionary
car_dict = thisdict.copy()
print(car_dict)

# sort dictionary
for x in sorted(car_dict):
    print(x)
print(car_dict[x])

my_family = {
    "child_1": {
        "name": "Anne",
        "birth_year": 2004,
        "allergy": False
    },
    "child_2": {
        "name": "Alex",
        "birth_year": 2007
    },
    "child_3": {
        "name": "John",
        "birth_year": 2011
    }
}
print()
for x, y in my_family.items():
    print(x)
for a, z in y.items():
    print("{}: {}".format(a, z))