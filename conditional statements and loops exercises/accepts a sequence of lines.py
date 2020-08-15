# Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output (all characters in lower case).

word_lower = lambda word : (word.replace(" ","")).lower()


print(word_lower("RAJ IS MY NAME "))		# rajismyname
print(word_lower("PYTHON"))					# python