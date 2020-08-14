# Write a Python program to find the second lowest grade of any student(s)
# from the given names and grades of each student using lists and lambda.

student = [
    {"name": "Raj", "marks": 97},
    {"name": "Raima", "marks": 91},
    {"name": "Monai", "marks": 77},
    {"name": "Babai", "marks": 87}
]

grade = lambda *args: [arg['marks']
                       for arg in sorted(student, key=lambda k:k['marks'])][1]

print(grade(*student))		# 87

student = [
    {"name": "Raj", "marks": 97},
    {"name": "Raima", "marks": 91},
    {"name": "Babai", "marks": 87}
]

print(grade(*student))		# 91