class Student:
    def __init__(self, marks1, marks2):
        self._marks1 = marks1
        self._marks2 = marks2

    def update_marks1(self, marks):
        self._marks1 = marks

    def update_marks2(self, marks):
        self._marks2 = marks

    def get_marks(self):
        return f"marks1:{self._marks1}, marks2:{self._marks2}"

    def __add__(self, other):
        res1 = self._marks1 + self._marks2
        res2 = other._marks1 + other._marks2
        return res1 + res2

    def __gt__(self, other):
        res1 = self._marks1 + self._marks2
        res2 = other._marks1 + other._marks2
        if res1 > res2:
            return "Student 1 wins"
        else:
            return "Student 2 wins"


Raj = Student(87, 91)
Raima = Student(88, 78)

print(Raj + Raima)
print(Raj > Raima)

print(Raima.get_marks())
Raima.update_marks1(91)
Raima.update_marks2(89)
print(Raima.get_marks())
print(Raj > Raima)