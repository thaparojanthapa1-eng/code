#include<stdio.h>
int addition(int, int); //prototype
int main()
{
    int num1, num2, result;
    printf("Enter two numbers");
    scanf("%d%d", &num1, &num2 );
    result=addition(num1, num2); //function call
    printf("Fnal sum=\t%d", result);
    return 0;
}

int addition(int x, int y) //definition
{
    int sum;
    sum=x+y; 
    return sum;
}