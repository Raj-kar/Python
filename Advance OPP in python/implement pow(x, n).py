class PowerOfNum:
    def __init__(self, num, pow):
        self.num = num
        self.pow = pow

    @property
    def get_num(self):
        return f"num = {self.num}, and power = {self.pow}"

    def calculate(self):
        return self.num ** self.pow


n1 = PowerOfNum(3, 5)
print(n1.calculate())
n2 = PowerOfNum(100, 0)
print(n2.calculate())
n3 = PowerOfNum(2, -3)
print(n3.calculate())

