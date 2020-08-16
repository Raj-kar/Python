import calculator

print(calculator.add(10,20))	# 30
print(calculator.sub(10,20))	# -10
print(calculator.mul(10,20))	# 200
print(calculator.div(10,20))	# 0.5


# call calculator my won module !..

# different calling techniques
# if you want to perfrom only sum

from calculator import add 

print(add(10,50))		# 60


# if you want to call functions in different name
from calculator import add as addition_of_two_no

print(addition_of_two_no(15,87))		# 102