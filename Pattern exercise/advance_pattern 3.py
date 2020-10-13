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

//Sneha Majumder


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

#include<stdio.h>
#include<conio.h>
int main()
{
		int i,j,k,l,sp,n;
		printf("\n Enter rows: ");
		scanf("%d",&n);
		sp=n-1;
		for(i=0;i<n-1;i++)
		{
			for(j=1;j<=sp;j++)
			{
				printf(" ");
			}
			for(k=i;k>=0;k--)
			{
				if(k%2==0)
				printf("1");
				else
				printf("0");
			}
			for(l=0;l<=i-1;l++)
			{
				if(l%2==0)
				printf("0");
				else
				printf("1");
			}
			printf("\n");
			sp--;
		}
		return 0;
}


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

#include<stdio.h>
#include<conio.h>
int main()
{
		int i,r,c,j;
		printf("\n Enter the number of rows: ");
		scanf("%d",&r);
		printf("\n Enter the number of columns: ");
		scanf("%d",&c);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
					if(j==0 || j==c-1 || i==0 || i==r-1)
					printf("0");
					else
					printf("1");
			}
			printf("\n");
		}
		return 0;
}


'''
* 0 0 0 * 0 0 0 *
0 * 0 0 * 0 0 * 0
0 0 * 0 * 0 * 0 0
0 0 0 * * * 0 0 0
'''


#include<stdio.h>
#include<conio.h>
int main()
{
		int i,r,j,c;
		printf("\n Enter number of rows: ");
		scanf("%d",&r);
		printf("\n Enter the number of columns: ");
		scanf("%d",&c);
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(j==i || j==(c-i-1) || j==c/2)
				printf("*");
				else
				printf("0");
			}
			printf("\n");
		}
		return 0;
}


'''
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
'''


#include<stdio.h>
#include<conio.h>
int main()
{
	int i,j,n;
	printf("\n Enter range:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
			for(j=0;j<n;j++)
			{
					if(j==i || j==(n-i-1))
					printf("1");
					else
					printf("0");
			}
			printf("\n");
	}
	return 0;
}
