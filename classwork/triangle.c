#include<stdio.h>
int main()
{
    int i,n,j;
    printf("Enter the number of layers you want in triangle");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}