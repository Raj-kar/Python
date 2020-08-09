def square_list(start=1, stop=1):
    return [i*i for i in range(start, stop+1)]


print(square_list(1, 10))
print(square_list(start=1, stop=30))
print(square_list())  # default value 1 return !
