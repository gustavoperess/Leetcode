
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *getSneakyNumbers(int *nums, int numsSize, int *returnSize)
{
    int maxVal = 1000;
    int *hashTable = calloc(maxVal, sizeof(int));
    int *items = malloc(sizeof(int) * numsSize);
    int count = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (hashTable[nums[i]] == 1)
        {
            items[count++] = nums[i];
        }
        hashTable[nums[i]]++;
    }
    items = realloc(items, sizeof(int) * count);
    *returnSize = count;
    free(hashTable);
    return items;
}

int main()
{
    int input[] = {0, 3, 2, 1, 3, 2};
    int len = sizeof(input) / sizeof(int);
    int returnSize;

    int *result = getSneakyNumbers(input, len, &returnSize);

    free(result);
    return 0;
}