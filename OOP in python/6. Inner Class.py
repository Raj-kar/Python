# If a class is within a class, that's called inner class.
# We may use an inner class when we want to add added functionality in a class.


class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(f"Student name {self.name} and roll {self.roll}")

    def laptop_config(self):
        print(
            f"Laptop brand {self.lap.brand},ram = {self.lap.ram}\
            Gb and a powerful {self.lap.gpu} processor")

    class Laptop:					# Inner Class
        def __init__(self):
            self.brand = "Asus"
            self.ram = 8
            self.gpu = "i5"


s1 = Student("Raj", 117)
# Student name Raj and roll 117
s2 = Student("Raima", 118)
# Student name Raima and roll 118

s1.show()
s2.show()


# Acess Inner class

print(s1.lap.brand)		# Asus
print(s1.lap.ram)		# 8

print(s2.lap.gpu)		# i5
print(s2.lap.brand)		# Asus

# Laptop brand Asus,ram = 8 Gb and a powerful i5 processor
print(s1.laptop_config())


# we can also acess inner class by this method

s_lap = Student.Laptop()

print(s_lap.brand)				# Asus
print(s_lap.ram)				# 8
print(s_lap.gpu)				# i5
