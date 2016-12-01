#include <stdio.h>
int main()
{
    int firstNumber, secondNumber, sumOfTwoNumbers;
    int *a = NULL;
    int b = 10;

    if(1)
    {
        for (i = 0; i < 2; ++i) {
            while(i < 2)
                printf("yellow\n");
            printf("some yellow\n");
        }

    }

    switch (b) {
        case 10:
            printf("ten\n");
        default:
            printf("not found\n");
    }


    if (a && 1)
    	printf("Enter two no., also : %d, addr: %p", (a & 1), &b);
    else if (a == NULL)
    	printf("Enter two integers: ");

    // Two integers entered by user is stored using scanf() function
    scanf("%d %d", &firstNumber, &secondNumber);

    // sum of two numbers in stored in variable sumOfTwoNumbers
    sumOfTwoNumbers = firstNumber + secondNumber;

    // Displays sum      
    printf("%d + %d = %d", firstNumber, secondNumber, sumOfTwoNumbers);

    return 0;
}