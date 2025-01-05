#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Given an integer n, return a string array answer (1-indexed) where:

// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.

char **fizzBuzz(int n, int *returnSize)
{

    char **arr = (char **)malloc(n * sizeof(char *));
    if (arr == NULL)
    {
        return NULL;
    }

    for (int i = 0; i <= n; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            arr[i] = strdup("FizzBuzz");
            // printf("FizzBuzz\n");
        }
        else if (i % 5 == 0)
        {
            arr[i] = strdup("Buzz");
            // printf("Buzz\n");
        }
        else if (i % 3 == 0)
        {
            arr[i] = strdup("Fizz");
            // printf("Fizz\n");
        }
        else
        {
            arr[i] = (char *)malloc(12 * sizeof(char));
            sprintf(arr[i], "%d", i); 
            // printf("%d\n", i);
        }
    }
    for (int i = 1; i <= n; i++)
    {
        printf("result[%d] = %s\n", i, arr[i]);
    }

    return 0;
}

int main()
{
    fizzBuzz(15, (int *)15);
    return 0;
}
