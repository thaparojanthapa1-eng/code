// #include<stdio.h>
// int main()
// {
//     int i;
//     for(i=1; i<=10; i++)
//     {
//         printf("Hello world\n");
//         if(i>=5)
//         {
//             break;
//         }
//     }
//     return 0;
// }

// #include<stdio.h>
// int main()
// {
//     int i;
//     for(i=1; i<=10; i++)
//     {
//         printf("Hello ");
//         if(i>=5)
//         {
//             continue;
//         }
//         printf("World\t");
//     }
//     return 0;
// }

#include<stdio.h>
int main()
{
    int i=1;
    a:
    printf("%d\t", i);
    i++;
    if(i<=10)
    {
        goto a;
    }
    return 0;
}