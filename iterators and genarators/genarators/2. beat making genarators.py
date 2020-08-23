# Lame function that returns a list of beats.
# Only runs 100 times
# def current_beat():
#     maximum = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < maximum:
#         if i >= len(nums):
#             i = 0
#         result.append(nums[i])
#         i += 1
#     return result

# Infinite Generator - returns one beat a time, no list used!

def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 1
        yield nums[i]
        i += 1


counter = current_beat()
print(next(counter), end=" ")
print(next(counter), end=" ")
print(next(counter), end=" ")
print(next(counter), end=" ")
# 1 2 3 4

print()
for num in range(10):
    print(next(counter), end=" ")   # 2 3 4 2 3 4 2 3 4 2
