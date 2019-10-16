class Circle():

    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def circumfrence(self):
        return self.radius * 2 * self.pi

# myCircle = Circle(10)
# print(myCircle.radius)
# print(myCircle.area())
# print(myCircle.circumfrence())

class Animal():
    def __init__(self, fur):
        self.fur = fur
        print('Animal Created!!')

    def eat(self):
        print('Eating Now!!')

    def report(self):
        print('Animal')

a = Animal('Fuzzy')
a.eat()
a.report()

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self, fur)
        print('Dog Ceated!!')

    def report(self):
        print('This is a Dog!!')

d = Dog("Fuzzy")
# d.eat()
# d.report()
print(d.fur)
