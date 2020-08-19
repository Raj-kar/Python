from math import factorial


class Factorial:
    def __init__(self, value):
        self.value = value

    def fact(self):
        return factorial(self.value)


test1 = Factorial(5)		# we pass value here
print(test1.fact())			# 120, we print it here !


test2 = Factorial(9)
print(test2.fact())			# 362880
