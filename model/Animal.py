class Animal:
    def __init__(self, species, location, size, color, group):
        self.species = species
        self.location = location
        self.size = size
        self.color = color
        self.group = group

    def print_animal(self):
        print(f'species: {self.species}, location: {self.location}, size: {self.size}, color: {self.color}, family: {self.family}')

