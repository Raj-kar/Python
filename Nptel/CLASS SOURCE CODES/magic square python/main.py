def solve(num):
    if num % 2 == 0:
        return "Odd number must be given !"

    magic_square = [[None]*num for i in range(num)]
    counter = 1
    row = num // 2
    col = num - 1

    while counter != (num*num + 1):
        if row == - 1 and col == num:
            row = 0
            col = num - 2
        elif row == - 1:
            row = num - 1
        elif col == num:
            col = 0
        elif magic_square[row][col] != None:
            ''
            row += 1
            col -= 2

        magic_square[row][col] = counter

        counter += 1
        row -= 1
        col += 1

    for row in magic_square:
        decorate(*row)


# outputs --->

solve(3)
"""
output -->
2 7 6
9 5 1
4 3 8
"""

# print(solve(4))
"""
output -->
Odd number must be given !
"""

# solve(5)
"""
output -->
9 3 22 16 15
2 21 20 14 8
25 19 13 7 1
18 12 6 5 24
11 10 4 23 17
"""

# solve(7)
"""
output -->
20 12 4 45 37 29 28
11 3 44 36 35 27 19
2 43 42 34 26 18 10
49 41 33 25 17 9 1
40 32 24 16 8 7 48
31 23 15 14 6 47 39
22 21 13 5 46 38 30
"""
