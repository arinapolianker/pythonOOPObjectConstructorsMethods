class Person:
    def __init__(self, first_name, last_name, age, gender, city, owned_animals):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.city = city
        self.owned_animals = owned_animals

    def print_person(self):
        print(f'name: {self.first_name} {self.last_name}, age: {self.age}, gender: {self.gender}, city: {self.city}')

    def add_animal(self, animal):
        if self.owned_animals is None:
            self.owned_animals = []
        if animal not in self.owned_animals:
            self.owned_animals.append(animal)
            print(f'{self.first_name} owns now a {animal.species}')
        else:
            print(f'{self.first_name} already owns this species.')

    def remove_animal(self, animal):
        if animal in self.owned_animals:
            self.owned_animals.remove(animal)
            print(f'{self.first_name} no longer owns a {animal.species}')
        else:
            print(f'{self.first_name} don`t owns a {animal.species}')