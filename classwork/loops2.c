#include<stdio.h>
int main()
{
    int i=2, isprime=1,num;
    printf("Enter a number:     ");
    scanf("%d",&num);
    while (i<=num/2)
    {
        if (num%i==0)
        {
            isprime=0;
            break;
        }
        i++;
    }
    if (isprime==1)
    {
        printf("The number is prime.");
    }
    else
    {
        printf("The number is not prime.");
    }
    return 0;
}