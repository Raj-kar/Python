'''
Week - 9 --> Programming solutions
Question 1 --> Digit
'''
digit = input()


def is_same(digit):
    return len(digit) == digit.count(digit[0])


def swap_values(digit, val, count):
    d = list(digit)
    d[count] = val
    return ''.join(d)


def check_digit(digit):
    count = 0
    while count < len(str(digit)):
        temp = digit
        if(digit[count] == '0'):
            digit = swap_values(digit, '1', count)
        else:
            digit = swap_values(digit, '0', count)
        if(is_same(digit)):
            return True
        digit = temp
        count += 1


if(check_digit(digit)):
    print("YES", end="")
else:
    print("NO", end="")

'''
Question 2 ---> Missing number
'''

nums = sorted(map(int, input().split(" ")))
last_digit = nums[len(nums)-1]
num_list = list(range(1, last_digit))


def find_missing(nums, all_nums):
    for i in range(len(nums)):
        if(nums[i]) != all_nums[i]:
            return all_nums[i]


print(find_missing(nums, num_list), end="")

'''
Question 3 ---> Rearrangement
'''

nums = sorted(map(int, input().split(" ")))

if(nums.count(-1) <= 1):
    print(*nums, end="")
else:
    max_num = max(nums)
    all_nums = list(range(max_num+1))
    for i in range(len(all_nums)):
        if all_nums[i] not in nums:
            all_nums[i] = -1
    print(*all_nums, end="")
