#include<stdio.h>
int greatest(int, int, int);
int main()
{
    int num1, num2, num3, greatestnumber;
    printf("Enter three numbers of your choice to find the greatest");
    scanf("%d%d%d", &num1, &num2, &num3);
    greatestnumber=greatest(num1, num2, num3);
    printf("The greatest number is %d", greatestnumber);
    return 0;
}

int greatest(int a, int b, int c)
{
    if(a>b && a>c)
    {
        return a;
    }
    else if (b>c)
    {
        return b;
    }
    else
    {
        return c; 
    }
}