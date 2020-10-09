def solve(num):
    if num % 2 == 0:
        # the numbers has to be odd for finding the magic sum !
        return "Odd number must be given !"

    # formula for finding magic number ! But not needed !
    # magic_num = num * (num**2 + 1) // 2
    magic_square = []
    counter = 1
    row = num // 2
    col = num - 1

    for i in range(0, num):
        # insert NULL values on the list ! Otherwise python will show out of index msg :(
        magic_square.append([])
        # if you are using JAVASCRIPT OR C,C++ you can skip this,
        for j in range(0, num):
            # because in C or Js we can enter value on any index !
            magic_square[i].append(None)

    # if user enter 3, the lopp will run from 1 to 10 (n-1)
    while counter != (num*num + 1):
        if row == - 1 and col == num:
            ''' If anytime row position becames -1 and column position became user_input,
                switch row to 0, and column to user_input - 2  '''
            row = 0
            col = num - 2
        elif row == - 1:
            ''' If anytime row position becames -1 , switch row to position to, user_input - 1  '''
            row = num - 1
        elif col == num:
            ''' If anytime column position becames user_input , switch column to position to, 0  '''
            col = 0
        elif magic_square[row][col] != None:
            ''' If there is alreay a value on the position, make increse row by 1 and decrese column by 2 '''
            row += 1
            col -= 2

        # insert counter at calculate row-column position !
        magic_square[row][col] = counter

        # insert the counter by 1 !
        counter += 1
        # then for calculate and insert the next value decrese row by 1, and increse column by 1.
        row -= 1
        col += 1

    # print the final magic box
    for row in magic_square:
        ''' *(astric) used here for unpack the list !
            example :: num = [1, 2, 3] and *num = 1, 2, 3    '''
        print(*row)


# outputs --->

solve(3)
"""
output -->
2 7 6
9 5 1
4 3 8
"""

print(solve(4))
"""
output -->
Odd number must be given !
"""

print(solve(5))
"""
output -->
9 3 22 16 15
2 21 20 14 8
25 19 13 7 1
18 12 6 5 24
11 10 4 23 17
"""

solve(7)
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
