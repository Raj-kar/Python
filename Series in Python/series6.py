# x^1/1! + x^2/2! + x^3/3! .... x^n/n!
import math

x = int(input("Enter value of x :: "))
num = int(input("Enter a range :: "))
sum = 0

for i in range(1,num+1):
    print(x**(i/math.factorial(i)))
    sum += x**(i/math.factorial(i))

print(sum)