
#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>

// The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

// F(0) = 0, F(1) = 1
// F(n) = F(n - 1) + F(n - 2), for n > 1.
// Given n, calculate F(n).

// Example 1:

// Input: n = 2
// Output: 1
// Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

// int fib(int n)
// {
//     int previousNumber = 0;
//     int nextNumber = 1;
//     int fibNumber = 0;
//     for (int i = 1; i < n; i++)
//     {
//         fibNumber = previousNumber + nextNumber;
//         previousNumber = nextNumber;
//         nextNumber = fibNumber;
//     }
//     return fibNumber;
// }

// now with recursion
int fib(int n)
{
    if (n == 1) return 1;
    if (n > 1)
        return fib(n - 1) + fib(n - 2);
    else
    {
        return 0;
    }
}

int main()
{
    int result = fib(10);
    printf("%d\n", result);
    return 0;
}
