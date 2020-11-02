'''
Week - 8 --> Programming solutions
Question 1 --> Repeat
'''
number = input()


def repeat(num):
    res = 0
    for i in num:
        res += int(i)
    return str(res)


while len(number) != 1:
    number = repeat(number)

print(number, end="")

'''
Another approach !
'''
number = int(input())


def is_single_digit(num):
    return (len(str(num))) == 1


def repeat(num):
    res = 0
    for i in str(num):
        res += int(i)

    if(is_single_digit(res)):
        print(res, end="")
    else:
        repeat(res)


repeat(number)

'''
Question 2 ---> Push
'''


def push_at_last(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)

    print(*arr, end="")


arr = list(map(int, input().split(" ")))

push_at_last(arr)
