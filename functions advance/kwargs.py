# save as a dict

def fav_color(**kwargs):
	for i,j in kwargs.items():
		print(f"{i} love {j}")

fav_color(raj="purple",raima="black",rahul="yellow")

#output:
# raj love purple
# raima love black
# rahul love yellowa