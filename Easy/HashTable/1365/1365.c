#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *smallerNumbersThanCurrent(int *nums, int numsSize, int *returnSize)
{
    int *items = calloc(numsSize, sizeof(int));
    for (int i = 0; i < numsSize; i++)
    {
        for (int y = 0; y < numsSize; y++)
        {
            if (nums[i] > nums[y])
            {
                items[i]++;
            }
        }
    }

    *returnSize = numsSize;

    return items;
}

int main()
{
    int input[] = {1, 8, 2, 2, 3};
    int len = sizeof(input) / sizeof(int);
    int returnSize;
    int *result = smallerNumbersThanCurrent(input, len, &returnSize);

    printf("\n");

    free(result);
    return 0;
}