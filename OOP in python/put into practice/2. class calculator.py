class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


test1 = Calculator(20, 10)
test2 = Calculator(50, 20)

print(test1.addition())				# 30
print(test1.subtraction())			# 10
print(test1.multiplication())		# 200
print(test1.division())				# 2.0


print(test2.addition())				# 70
print(test2.subtraction())			# 30
print(test2.multiplication())		# 1000
print(test2.division())				# 2.5

# no need to pass value everytime.
# pass it once, it class. It'll hold the values using Self
