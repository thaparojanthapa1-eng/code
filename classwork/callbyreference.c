#include<stdio.h>
void swap(int *, int *);
int main()
{
    int num1=10, num2=20;
    swap(&num1, &num2);
    printf("num1=%d, num2=%d", num1, num2);
    return 0;
}

void swap(int *x, int *y)
{
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
}