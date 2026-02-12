#include<stdio.h>
#include<stdlib.h>
int main()
{
float num1,num2,result;
int choice;
while (1)
{
    printf("\nEnter two numbers: ");
    scanf("%f%f", &num1, &num2);
    printf("\n1. addition\n2. subtraction\n3. multiplication\n4. division\n 5.exit");
    printf("\nEnter your choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
        case 1:
            result=num1+num2;
            printf("Addition is %f", result);
            break;
        case 2:
            result=num1-num2;
            printf("Subtraction is %f", result);
            break;
        case 3:
            result=num1*num2;
            printf("Multiplication is %f", result);
            break;
        case 4:
            result=num1/num2;
            printf("Division is %f", result);
            break;
        case 5:
            break;
        default:
            printf("Invalid choice");
    }
}
return 0;
}