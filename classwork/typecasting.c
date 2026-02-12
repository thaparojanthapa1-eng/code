#include<stdio.h>
// #include<math.h>
int power(int, int);
int main()
{
    int r;
    r=power(2,9);
    printf("%d", r);
    return 0;
}

int power(int a, int b)
// {
//     int r=1, i;
//     for(i=1; i<=b; i++)
//     {
//         r=r*a;
//     }
//     return 0;
// }
{
    int r=1;
    while(b>=1)
    {
        r=r*a;
        b-=1;
    }
    return r;
}