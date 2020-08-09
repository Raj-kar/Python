def name(fname = "python" , lname = "is awesome"):  #set default value to fname and lname
	return f"Hey, Welcome {fname} {lname}"

print(name())  # without passing argument
print(name("Raj","kar"))   # passing argument
print(name(lname="Kar",fname="Raj"))   # with keyword argument

