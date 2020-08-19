

class Person:
    def __init__(self):
        self.name = "Raj"
        self.age = 19

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


# constructor
emp_1 = Person()
emp_2 = Person()

# both have same name "Raj" and age 19
print(emp_1.name)
print(emp_2.name)

# but both have different memory location because they're two different obj
print(id(emp_1))
print(id(emp_2))

# compare obj 1 age with obj 2 age [here obj is emp1 and emp2]
# Here both are same
if emp_1.compare(emp_2):
    print("They are same")
else:
    print("They are different")


# change emp1 age to 30
# now they are different
emp_1.age = 30
if emp_1.compare(emp_2):
    print("They are same")
else:
    print("They are different")
