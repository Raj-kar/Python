matrix = [[25, 1, 29, 7],
          [24, 20, 4, 32],
          [16, 38, 29, 1],
          [48, 25, 21, 19]
          ]


matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


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
