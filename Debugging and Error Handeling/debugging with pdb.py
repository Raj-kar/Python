# FIRST EXAMPLE:
# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


# Be careful with variable names, Don't use like a,l,n etc. 
# If you use these types of names it may be conflict with the pdb default keywords !
def add_numbers(num1, num2, num3, num4):
    import pdb; pdb.set_trace() 

    return num1 + num2 + num3 + num4
add_numbers(1,2,3,4) 

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

