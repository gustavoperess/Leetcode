
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// brute force
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    *returnSize = 2;
    int *arr = malloc((*returnSize) * sizeof(int));
    if (arr == NULL)
    {
        return NULL;
    }
    for (int i = 0; i < numsSize - 1; i++)
    {
        for (int y = i + 1; y < numsSize; y++)
        {
            if (nums[i] + nums[y] == target)
            {
                arr[0] = i;
                arr[1] = y;
                return arr;
            }
        }
    }
    free(arr);
    return NULL;
}

int main()
{
    int numbers[] = {2, 7, 11, 15};
    int numsSize = sizeof(numbers) / sizeof(numbers[0]);
    int returnSize;
    int *result = twoSum(numbers, numsSize, 9, &returnSize);
    if (result != NULL)
    {
        printf("Indices: [%d, %d]\n", result[0], result[1]);
        free(result); // Free the allocated memory for the result array
    }
    else
    {
        printf("No solution found.\n");
    }
    return 0;
}