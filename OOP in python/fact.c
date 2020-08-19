#include<stdio.h>

int recursive_fact(int num);
int iteration_fact(int num);
int main()
{
	int num,f1,f2;
	
	printf("Enter a value to cheak factorail:: ");
	scanf("%d",&num);
		
	f1=iteration_fact(num);
	printf("\n FACTORIAL using iteration = %d",f1);
	
	f2=recursive_fact(num);
	printf("\n FACTORIAL using recursive = %d",f2);
}

int iteration_fact(int num){
	int f=1;
	
	for(int i=1;i<=num;i++){
		f=f*i;
	}
	
	return f;
}

int recursive_fact(int num)
{
	if(num == 0 || num == 1)
		return 1;
	else
		return (num*recursive_fact(num-1));
}