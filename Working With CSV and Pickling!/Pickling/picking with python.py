import pickle


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

# here wb stands for write binary
with open("save_pet.pickle", "wb") as file:
    pickle.dump(cat, file)

# here rb stands for read binary
with open("save_pet.pickle", "rb") as file:
    cat_data = pickle.load(file)
    print(cat_data)
    print(cat_data.fav_toy())

# dumps multiple files
with open("save_pet_2.pickle", "wb") as file:
    pickle.dump((cat, dog), file)

# loads multiple files
with open("save_pet_2.pickle", "rb") as file:
    cat_data, dog_data = pickle.load(file)
    print(cat_data)
    print(dog_data)
    print(cat_data.fav_toy())
    print(dog_data.fav_toy())
