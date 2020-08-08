
num = input("how many emoji you want ??")

num = int(num)

#loical mehtod

# for i in range(num):
# 	for j in range(i,0,-1):
# 		print("\U0001f600",end="")
# 	print("")


#using For

# for i in range(1,num+1):
# 	print("*"*i)


# using While

# start = 1

# while start <= num:
# 	print("*"*start)
# 	start+=1

#repeated time if user want 

# repeated = input("How many times you want to repeat ::")
# repeated = int(repeated)

# if(repeated == 0):
# 	for i in range(1,num+1):
# 		print("*"*i)
# else:
# 	for i in range(repeated+1):
# 		for i in range(1,num+1):
# 			print("*"*i)

# with out string multiplication - ugly
# for i in range(1,num+1):
# 	count = 1
# 	pattern = ""
# 	while count <= i :
# 		pattern += "*"
# 		count += 1
# 	print(pattern)


# like trangle - not complete

# for i in range(1,num+1):
# 	for j in range(num,num>=i,-1):
# 		print(" "*j,end="")
# 		print("*"*i)