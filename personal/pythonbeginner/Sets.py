animals = {"dogs", "cats", "tiger", "elepahants", "dogs"}
wild_animals1 = ["leopard", "elephant", "lion"]
animals.add("monkey")
animals.update(wild_animals1, {"dolphin"})
animals.discard("dogs")
print(animals)
print("monkey" in animals)


animals1 = set(["dogs", "cats", "tiger", "elepahants", "dogs"])
print(animals1)
animals1.clear()
print(animals1)

wild_animals = {"tiger", "lion", "elephant"}
domestic_animals = {"dog", "cat", "elephant"}

all_animals = wild_animals.union(domestic_animals)
print(all_animals)

common_animals = domestic_animals.intersection(wild_animals)
print(common_animals)