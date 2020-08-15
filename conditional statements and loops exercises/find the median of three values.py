# Write a Python program to find the median of three values.

# Expected Output:
# Input first number: 15                                                  
# Input second number: 26                                                 
# Input third number: 29                                                  
# The median is 26.0   

x,y,z = input("Input three Number :: ").split()

print(sorted([x,y,z])[1])
