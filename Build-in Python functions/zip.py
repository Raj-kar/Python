midterms = [80,91,78]
finals = [98,89,53]
students = ['Raj', 'Raima', 'Moani']


# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)































# # r = dict(zip(students, midterms))
# print(r)

# r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
# print(r)

# r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
# print(r)


# z = zip(
# 	students,
# 	map(
# 		lambda pair: max(pair),
# 		zip(midterms, finals)
# 	)
# )

