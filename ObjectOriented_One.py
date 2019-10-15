class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = 'mamal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

x = Dog('Sammy', 'Huskie')

print(x.name)
print(x.breed)
print(x.species)
