def prime(limit):
	for i in range(2,limit):
		count = 0
		for j in range(2,i):
			if i % j == 0:
				count += 1
		
		if count == 0:
			print(i,end=" ")


prime(5) # prime between 0 to 5
print()
prime(10) # prime between 0 to 10
print() 
prime(50) # prime between 0 to 50