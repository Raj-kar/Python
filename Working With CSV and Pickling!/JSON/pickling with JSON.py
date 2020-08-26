import jsonpickle


class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']

    def __init__(self, name, species, toy):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        self.toy = toy

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.species = species

    def fav_toy(self):
        return f"{self.name} play withs {self.toy} !"


cat = Pet("Blue", "cat", "Strings")
dog = Pet("Wyatt", "dog", "Ball")

# Open a file and write
with open("pet_data.json", "w") as file:
    data = jsonpickle.encode(cat)
    file.write(data)

# Open a file and read
with open("pet_data.json") as file:
    json_read = file.read()
    data = jsonpickle.decode(json_read)
    print(data)
    print(data.fav_toy())
