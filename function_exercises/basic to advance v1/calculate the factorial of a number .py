
def prime(num):
    num = str(num)
    flag = 0
    for i in num:
        i = int(i)
        for j in range(2, i):
            if i % j == 0:
                print(f"{i} is not a prime number")
               	flag = 1
        if(i == 1):
            print(f"{i} is not either a prime number or non-prime number")
        elif(flag != 1):
            print(f"{i} is a prime number")


# prime(179)
print()
prime(159)