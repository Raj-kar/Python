'''
Week - 7 --> Programming solutions
Question 1 --> Print Pattern
'''

num = int(input())
pattern = []

for row in range(1, num+1):
    pattern.append([])
    for col in range(1, row+1):
        pattern[row - 1].append(col)

for i in pattern:
    print(*i)


'''
Question 2 ---> Rotate Matrix by 90 degree by moving one element
credit :- @GFG
'''


def rotateMatrix(mat):

    if not len(mat):
        return

    """ 
        top : starting row index 
        bottom : ending row index 
        left : starting column index 
        right : ending column index 
    """

    top = 0
    bottom = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and top < bottom:

        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]

        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat


def printMatrix(mat):
    for row in mat:
        print(row)


n = int(input())
arr = []

for row in range(n):
    arr.append(input().split())

matrix = rotateMatrix(arr)
# Print modified matrix
for row in matrix:
    print(*row)

'''
Question 3 ---> Counter Spiral
'''


def counter_spiral(arr):
    start_row, end_row, start_column, end_column = 0, len(
        arr[0]) - 1, 0, len(arr[0]) - 1

    while(start_row <= end_row and start_column <= end_column):
        for i in range(start_row, end_row + 1):
            print(arr[i][start_column], end=" ")
        start_column += 1

        for i in range(start_column, end_column + 1):
            print(arr[end_row][i], end=" ")
        end_row -= 1

        for i in range(end_row, start_row - 1, -1):
            print(arr[i][end_column], end=" ")
        end_column -= 1

        for i in range(end_column, start_column - 1, -1):
            print(arr[start_row][i], end=" ")
        start_row += 1


n = int(input())
arr = []

for row in range(n):
    arr.append(input().split())


counter_spiral(arr)
