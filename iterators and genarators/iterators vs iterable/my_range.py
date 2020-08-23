class Counter:
    def __init__(self, lb=0, ub=0, step=1):
        self.start = lb
        self.end = ub
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= 0:
            if self.start < self.end:
                n = self.start
                self.start += self.step
                return n
            raise StopIteration
        else:
            if self.start > self.end:
                n = self.start
                self.start -= abs(self.step)
                return n
            raise StopIteration


for i in Counter(10, 20):
    print(i, end=" ")
print()
for i in Counter(10, 20, 2):
    print(i, end=" ")
print()
for i in Counter(20, 10, -1):
    print(i, end=" ")
print()
for i in Counter(20, 10, -2):
    print(i, end=" ")

# 10 11 12 13 14 15 16 17 18 19
# 10 12 14 16 18
# 20 19 18 17 16 15 14 13 12 11
# 20 18 16 14 12
