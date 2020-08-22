class Human:

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age	
		# self._color = "blue"					# use _(underscore) for private var

	# update and fetch age using getter and setter

	# getter
	@property
	def age(self):
		return self._age

	# setter
	@age.setter
	def age(self, new_age):
		if new_age > 0:
			self._age = new_age
		else:
			 raise ValueError("Age can't be Negative !")

	# update and fetch full_name using getter and setter

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")

	@property
	def fav_color(self):
		return self._color

	@fav_color.setter	
	def fav_color(self, color):
		self._color = color


	
h1 = Human("Raj", "kar", 19)

print(h1.__dict__)
print(h1.age)		# get the age without using parenthices
h1.age = 22			# set the age without using parenthices
print(h1.age)		# get the new age

print(h1.full_name)			# get the full name without using parenthices
h1.full_name = "Rahul kar"	# set the full name without using parenthices
print(h1.full_name)			# get the full name

h1.fav_color = "red"
print(h1.fav_color)
print(h1.__dict__)