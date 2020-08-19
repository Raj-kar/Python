

class Car:
    wheel = 4
    # Class/Static variables, we declare these because it's remain same for every obj.
    # Like here every has has four wheels, 2 mirror - Like this !
    # we are n't genarally changes these varible.
    # by changing the class variables [Car.wheel = 5] every car assign with
    # five wheels

    def __init__(self):
        # Instance variables, because different object has different property
        # as here different car has different mileage and name !
        # we genearlly change instance variables .
        self.mil = 20
        self.name = "BMW"


c1 = Car()
c2 = Car()

print(
    f"Car 1 name {c1.name}, mileage of {c1.mil} \
    km and has {c1.wheel} wheels")
print(
    f"Car 2 name {c2.name}, and mileage of {c2.mil}\
     km and has {c2.wheel} wheels")
# Car 1 name BMW, mileage of 20 km and has 4 wheels
# Car 2 name BMW, and mileage of 20 km and has 4 wheels

# if we change classic variable

Car.wheel = 5

print(
    f"Car 1 name {c1.name}, mileage of {c1.mil} \
     km and has {c1.wheel} wheels")
print(
    f"Car 2 name {c2.name}, and mileage of {c2.mil} \
     km and has {c2.wheel} wheels")
# Car 1 name BMW, mileage of 20 km and has 5 wheels
# Car 2 name BMW, and mileage of 20 km and has 5 wheels
