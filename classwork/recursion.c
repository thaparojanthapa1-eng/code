#include<stdio.h>
int factorial(int);
int main()
{
    int n, Factorial;
    printf("Enter number to find factorial: ");
    scanf("%d", &n);
    if(n<0)
    {
        printf("Invalid number");
    }
    else
    {
        Factorial=factorial(n);
        printf("The factorial is:   %d", Factorial);
    }
    return 0;
}

int factorial(int n)
{
    if(n==1 || n==0)
    {
        return 1;
    }
    else
    {
        return n*factorial(n-1);
    }
}
