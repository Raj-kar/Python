def traingle(row):
    count = 0
    space = row - 1

    for i in range(1, row*2, 2):
        for k in range(space):
            print(" ", end="")
        space -= 1
        for j in range(1, i+1):
            if count % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
            count += 1
        print()


traingle(10)

'''
         1
        010
       10101
      0101010
     101010101
    01010101010
   1010101010101
  010101010101010
 10101010101010101
0101010101010101010
'''


def hollow(row, column):
    for i in range(row):
        for j in range(column):
            if j == 0 or j == column - 1 or i == 0 or i == row - 1:
                print(0, end=" ")
            else:
                print(1, end=" ")
        print()


hollow(10, 20)
'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''


def moving_star(row):
    column = (row * 2) + 1

    for i in range(row):
        for j in range(column):
            if j == i or j == column - i - 1 or j == column // 2:
                print("*", end=" ")
            else:
                print(0, end=" ")
        print()


moving_star(4)
'''
* 0 0 0 * 0 0 0 *
0 * 0 0 * 0 0 * 0
0 0 * 0 * 0 * 0 0
0 0 0 * * * 0 0 0
'''


def criss_corss(num):
    for i in range(num):
        for j in range(num):
            if j == i or j == num - i - 1:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()


criss_corss(5)
'''
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
'''


# ---------------  © All copyrights reserved by Raj -------------------- #
''' you can add your own solution here  ;) '''

#       Contributed by Samwit Adhikary (Logic in C)         #



#include<stdio.h>
void hollow(int, int);

void main()
{
    int row, column;

    printf("Enter the value of Row: ");
    scanf("%d", &row);
    
    printf("Enter the value of Column: ");
    scanf("%d", &column);

    hollow(row,column);
}

void hollow(int row, int column)
{
    int i,j;
    for(i = 0; i <= row; i++)
    {
        for(j = 0; j <= column; j++)
        {
            if(i == 0 || i == row || j == 0 || j == column)
            {
                printf("0");
            }
            else
            {
                printf("1");
            }
        }
        printf("\n");
    }
}

#<--------------------------- Pattern Hollow completed ------------------------->

#include<stdio.h>
void criss_cross(int);

void main()
{
    int n;

    printf("Enter Number: ");
    scanf("%d", &n);

    criss_cross(n);
}

void criss_cross(int n)
{
    int i, j;

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(j == i || j == n - i - 1)
            {
                printf("1");
            }
            else
            {
                printf("0");
            }
        }
        printf("\n");
    }
}
#<------------------------Pattern Criss_Cross Completed-------------------> `

#include<stdio.h>
void moving_star(int);

void main()
{
    int n;
    printf("Enter Value of n: ");
    scanf("%d", &n);

    moving_star(n);
}

void moving_star(int row)
{
    int column, i, j;
    column = (row * 2) + 1;

    for(i = 0; i < row; i++)
    {
        for(j = 0; j < column; j++)
        {
            if(j == i || j == column - i - 1 || j == column / 2)
                printf("*");
            else
                printf("0");
        }
        printf("\n");
    }
}
#<-------------------- Moving Star Completed -------------->
