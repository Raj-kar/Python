mid_marks = [89, 91, 23]
final_marks = [99, 76, 89]
students = ["Raj", "Raima", "Monai"]

final_grade = dict(zip(
	students,
	map(
		lambda marks: max(marks),
		zip(mid_marks, final_marks)
	)
)
)
print(final_grade)
