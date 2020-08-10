# Write a function called showNumbers that takes a parameter called limit.
# It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# For example, if the limit is 3, it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD


def showNumbers(limit):
    limit_list = [[i, "Even"] if i % 2 == 0 else [i, "Odd"]
                  for i in range(limit+1)]
    for i in limit_list:
        print(i[0], end=" ")
        print(i[1])


showNumbers(3)
