'''
Week - 5 --> Programming solutions
Question 1 --> Dict Sqaure
'''
# using basic method
n = int(input())
square = {}

for i in range(1, n+1):
    square[i] = i * i


print(square, end="")

# using Dictionary Comprehension
n = int(input())
square_dict = {num: num*num for num in range(1, n+1)}
print(square_dict, end="")

'''
Question 2 --> Robot problem 
Original Credit - @Stack-Over-flow
'''

pos = {"x": 0, "y": 0}
num = int(input())

for _ in range(num):
    # ACCEPT MOVEMENT COMMAND AND STORE AS A LIST
    command = input().upper().split(" ")
    if command[0] == "UP":             # EXTRACT DIRECTION AND COMPARE
        # INCREMENT/DECREMENT APPROPRIATE CO-ORDINATES
        pos["y"] += int(command[1])
    if command[0] == "DOWN":
        pos["y"] -= int(command[1])
    if command[0] == "LEFT":
        pos["x"] -= int(command[1])
    if command[0] == "RIGHT":
        pos["x"] += int(command[1])

print(int(round((pos["x"]**2 + pos["y"]**2)**0.5)),
      end="")   # DISTANCE FROM ORIGIN

''' you can also use this formula for calculate DISTANCE !
import math
print(round(math.sqrt(pos["x"]**2 + pos["y"]**2)), end="")
'''


'''
Question 3 --> Dict Sqaure [same as previous]
'''
# using basic method
n = int(input())
square = {}

for i in range(1, n+1):
    square[i] = i * i


print(square, end="")

# using Dictionary Comprehension
n = int(input())
square_dict = {num: num*num for num in range(1, n+1)}
print(square_dict, end="")
