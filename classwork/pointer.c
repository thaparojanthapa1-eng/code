#include<stdio.h>
void swap(int *, int *);
int main()
{
    int a=10, b=15;
    swap(&a, &b);
    printf("\na=%d\nb=%d", a, b);
    return 0;
}

void swap(int *x, int *y)
{
    int temp;
    temp=*x;
    *x=*y;
    *y=temp;
}