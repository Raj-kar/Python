# Write a Python program to sort a list of dictionaries using Lambda.


sort_list = lambda l: print(sorted(l, key=lambda n: n['Roll']))  # sort by Roll no


st = [	{"name": "Raj", "Roll": 1},
       {"name": "Raima", "Roll": 2},
       {"name": "Moani", "Roll": 3}
       ]

sort_list(st)
# [{'name': 'Raj', 'Roll': 1}, {'name': 'Raima', 'Roll': 2}, {'name': 'Moani', 'Roll': 3}]


sort_list = lambda l: print(sorted(l, key=lambda n: n['name']))  # sort by Alphabte


sort_list(st)
# [{'name': 'Moani', 'Roll': 3}, {'name': 'Raima', 'Roll': 2}, {'name': 'Raj', 'Roll': 1}]
