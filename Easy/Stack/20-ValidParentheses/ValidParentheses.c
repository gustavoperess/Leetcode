
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

bool isValid(char *s)
{
    int l = strlen(s);
    char stack[l];
    int top = -1;
    for (int i = 0; i < l; i++)
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
        {
            stack[++top] = s[i];
        }
        else
        {
            if (top == -1) return false;

            char topChar = stack[top--];
            printf("stack -> %c\n", topChar);

            if ((s[i] == ')' && topChar != '(') ||
                (s[i] == '}' && topChar != '{') ||
                (s[i] == ']' && topChar != '['))
                return false;
        }
    }

    return top == -1;
}

int main()
{
    char input[] = "(]";
    isValid(input);
    return 0;
}