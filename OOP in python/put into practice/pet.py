class Pet:
	allowed = ['cat','dog','rat','bird','fish']

	def __init__(self, name, species, sound):
		if species in Pet.allowed:
			self.name = name
			self.species = species
			self.sound = sound
		else:
			raise ValueError(f"{species} is not a pet")

	def change_species(self, species):
		if species in Pet.allowed:
			self.species = species
		else:
			raise ValueError(f"{species} is not a pet")

	def change_name(self, new_name):
		self.name = new_name

	def loves(self, food):
		return f"{self.name} loves {food}"

	def pet_sound(self):
		return f"{self.name} sounds {self.sound}"



			

p1 = Pet("Blue", "dog", "bark")
p2 = Pet("jerry", "cat", "meow")

print(p1.species)

p1.change_species("rat")

print(p1.species)

print(p2.loves("fish"))

print(p2.name)

p2.change_name("tom")

print(p2.name)

print(p1.pet_sound())
print(p2.pet_sound())

print(id(p1.allowed))
print(id(p2.allowed))
print(id(Pet.allowed))