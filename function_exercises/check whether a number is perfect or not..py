def perfect(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    if(s == num):
        return True
    else:
        return False

print(perfect(496))
print(perfect(6))
print(perfect(28))

print(perfect(12))