
# for i in range(1,21):
# 	if(i == 4 or i == 13 ):
# 		print(f"{i} is Unlucky")
# 	elif(i % 2 == 0):
# 		print(f"{i} is even ")
# 	else:
# 		print(f"{i} is odd ") 

#after Refactor !

for i in range(1,21):
	if(i == 4 or i == 13 ):
		state = "Unlucky"
	elif(i % 2 == 0):
		state = "even"
	else:
		state = "odd"
	print(f"{i} is {state} ") 