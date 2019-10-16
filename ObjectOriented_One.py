class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = 'mamal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

x = Dog('Sammy', 'Huskie')
new_x = Dog('Cindy', 'Retriever')

print(x.name)
print(x.breed)
print(x.species)
print(new_x.breed)
print(new_x.name)
print(new_x.species)
