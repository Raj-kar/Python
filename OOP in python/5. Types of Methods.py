# There are three types of methods in a python class.
# Static, Class, and instance method.
# In Python variables, static and class are the same but not in methods.

from datetime import datetime


class Student():
    school_name = "Raj University"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):			# instance method [that use instance obj ]
        return round((self.m1 + self.m2 + self.m3) / 3, 2)

    @classmethod				# class method [that use class]
    def getSchoolName(cls):
        return cls.school_name

    @staticmethod				# static method [that doesn't use any self or cls !]
    def current_date_time():
        print(datetime.now())


s1 = Student(87, 85, 97)
s2 = Student(81, 95, 77)

print(s1.average())			# 89.67
print(s2.average())			# 84.33

# 2020-08-18 01:44:17.399573 [current date and time - when run the progarm]
Student.current_date_time()
