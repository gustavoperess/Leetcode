
#include <stdio.h>
#include <stdlib.h>
// Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

// A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

int *buildArray(int *nums, int numsSize, int *returnSize)
{
    int *numbers = malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++)
    {
        numbers[i] = nums[nums[i]];
    }
    *returnSize = numsSize;
    return numbers;
}

int main()
{
    int nums[] = {0, 2, 1, 5, 3, 4};
    int len = sizeof(nums) / sizeof(int);
    int returnSize;

    // int *result = buildArray(nums, len, &returnSize);
    // free(result);
     while (1) {
        int *result = buildArray(nums, len, &returnSize);
        if (!result) {
            printf("Memory allocation failed\n");
            break;
        }
        // Do not free the result to simulate memory fill-up
    }
    return 0;
}