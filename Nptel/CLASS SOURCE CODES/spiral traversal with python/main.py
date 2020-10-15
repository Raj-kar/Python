def spiral(n):
    result = [[None] * n for i in range(n)]

    counter = 1
    startRow = 0
    startColumn = 0
    endRow = n - 1
    endColumn = n - 1

    while startRow <= endRow and startColumn <= endColumn:
        for i in range(startColumn, endColumn + 1):
            result[startRow][i] = counter
            counter += 1
        startRow += 1

        for i in range(startRow, endRow + 1):
            result[i][endColumn] = counter
            counter += 1
        endColumn -= 1

        for i in range(endColumn, startColumn - 1, -1):
            result[endRow][i] = counter
            counter += 1
        endRow -= 1

        for i in range(endRow, startRow - 1, -1):
            result[i][startColumn] = counter
            counter += 1
        startColumn += 1

    for row in result:
        print(*row)


spiral(3)
spiral(4)
spiral(5)

'''
1 2 3
8 9 4
7 6 5
< -------------------------- >
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
< -------------------------- >
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
