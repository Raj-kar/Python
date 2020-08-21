class Person(object):
	
	active_user = 0

	def __init__(self, first, last, age):
		Person.active_user += 1
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def short_name(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, item):
		return f"{self.full_name()} likes {item}."

	def is_young(self):
		return self.age < 20

	def logout(self):
		Person.active_user -= 1
		return f"{self.first} logged out !"

	def happy_birthday(self):
		self.age += 1
		return f"Hey {self.first}! Happy Birthday :)"

	@classmethod
	def no_of_user(cls):
		return f"No of active user {cls.active_user}"



print(Person.no_of_user())

p1 = Person("Raj", "Kar",25)
p2 = Person("Monai", "Roy",16)

print(Person.no_of_user())

print(p1.full_name())
print(p2.short_name())

print(p1.is_young())
print(p2.is_young())

print(p2.logout())

print(Person.no_of_user())

print(p1.age)
print(p1.happy_birthday())
print(p1.age)

print(p1.likes("ice creme"))
print(p2.likes("cocacola"))