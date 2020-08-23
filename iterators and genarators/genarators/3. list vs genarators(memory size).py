# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(maximum):
    nums = []
    a, b = 0, 1
    while len(nums) < maximum:
        nums.append(b)
        a, b = b, a + b
    return nums


# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(maximum):
    x = 0
    y = 1
    count = 0
    while count < maximum:
        x, y = y, x + y
        yield x
        count += 1


for n in fib_gen(8):
    print(n, end=" ")
