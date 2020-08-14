# Write a Python program to find the second lowest grade of any student(s)
# from the given names and grades of each student using lists and lambda.
# Input number of students, names and grades of each student.

user_range = int(input("Enter how much number you want to enter :: "))

student_name = [];
student_marks = [];

for i in range(user_range):
	print(f"\n Enter name of student {i+1}: ",end= " ")
	student_name.append(input())
	print(f"\n Enter marks of student {i+1}: ",end= " ")
	student_marks.append(int(input()))

std_data = dict(zip(student_name,student_marks))

grade = lambda **args: sorted(std_data.values())[1]

print(f"\n Second Lowest marks is: {grade(**std_data)}")


