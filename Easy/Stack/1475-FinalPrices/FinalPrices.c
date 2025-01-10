#include <stdio.h>
#include <stdlib.h>

// You are given an integer array prices where prices[i] is the price of the ith item in a shop.

// There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

// Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount

// O(n^2) as I am looping twice.
// int *finalPrices(int *prices, int pricesSize, int *returnSize)
// {
//     int *discounts = malloc(sizeof(int) * pricesSize);
//     for (int i = 0; i < pricesSize; i++)
//     {
//         int found = 0;
//         for (int j = i + 1; j < pricesSize; j++)
//         {
//             if (i < j && prices[i] >= prices[j])
//             {
//                 found = 1;
//                 discounts[i] = abs(prices[i] - prices[j]);
//                 break;
//             }
//         }
//         if (found == 0)
//         {
//             discounts[i] = prices[i];
//         }
//     }
//     *returnSize = pricesSize;
//     return discounts;
// }

int *finalPrices(int *prices, int pricesSize, int *returnSize)
{
    int stk[pricesSize + 1], stkSize = 0;
    stk[stkSize++] = 0;

    for (int i = pricesSize - 1; i >= 0; i--)
    {
        while (stk[stkSize - 1] > prices[i])
            stkSize--;
        int discount = stk[stkSize - 1];
        stk[stkSize++] = prices[i];
        printf("discount %d\n", discount);
        prices[i] -= discount;
    }
    for(int i =0 ; i < pricesSize; i++) {
        printf("final result -> %d\n", prices[i]);
    }
    *returnSize = pricesSize;
    return prices;
}

int main()
{
    int prices[] = {8, 4, 6, 2, 3};
    int len = sizeof(prices) / sizeof(int);
    finalPrices(prices, len, prices);
    return 0;
}