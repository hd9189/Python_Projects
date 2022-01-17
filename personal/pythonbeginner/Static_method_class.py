class Dog:

    #variables used in differnet functoins
    dogs = []

    def __init__ (self, name):
        self.name = name
        self.dogs.append(self)

    # cls referes to class itself.
    @classmethod #tells program that its a type of method, so that it doesnt bug you
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    #nothing to do with class
    def bark(n):
        '''barks n times'''
        for _ in range(n):
            print("bark")

    def __str__(self):
        return "(" + str(self.name) + ")"

tim = Dog("tim")
print(Dog.dogs)
print(tim.num_dogs())
Dog.bark(5)
print(tim)
