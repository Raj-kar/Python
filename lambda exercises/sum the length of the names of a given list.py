# Write a Python program that sum the length of the names of a given list of names
# after removing the names that starts with an lowercase letter. Use lambda function.

sum_of_str = lambda *string: sum([len(val) for val in string if val[0] != val[0].lower()])


print(sum_of_str(*["Css","html","Python","java","Ruby","JQuery"])) 		# 19



sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

print(sum_of_str(*sample_names))										# 16