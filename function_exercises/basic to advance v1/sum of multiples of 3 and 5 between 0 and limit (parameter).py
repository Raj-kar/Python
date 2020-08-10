# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def multiples(limit):
    s = 0
    for i in range(1, limit):
        if 3*i < limit:
            print(3*i, end=" ")
            s += 3*i
        if 5*i <= limit:
            print(5*i, end=" ")
            s += 5*i
    return s

print(f"\n sum of the values = {multiples(20)}")
