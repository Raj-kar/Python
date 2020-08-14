
sentence = input("Enter a sentence :: ")

word = input("Enter a word for search :: ")

search = lambda word : True if word in sentence else False


if(search(word) == True):
	print("Word found ...!")
else:
	print("No word found")








