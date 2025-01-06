
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

// Return the score of s.

int scoreOfString(char *s)
{
    int length = strlen(s);
    int cal = 0;
    for (int i = 0; i < length - 1; i++)
    {
        cal += abs(s[i] - s[i + 1]);
    }
    return cal;
}

int main()
{
    scoreOfString("hello");
    return 0;
}