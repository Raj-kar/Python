# def find_max(num1,num2,num3):
# if(num1 > num2 and num1 > num3):
# return num1
# elif(num2 > num1 and num2 > num3):
# 	return num2
# return num3 #no need of return statement


# print(find_max(1,2,3))
# print(find_max(2,1,3))
# print(find_max(3,2,1))

# another method
def find_max_of_two(num1, num2):
    if num1 > num2:
        return num1
    return num2


def find_max_of_three(num1, num2, num3):
    return find_max_of_two(num1, find_max_of_two(num2, num3))


print(find_max_of_three(2, 4, 1))
