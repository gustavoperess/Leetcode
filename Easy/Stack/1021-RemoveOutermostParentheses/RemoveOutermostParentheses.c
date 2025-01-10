
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
// A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

// For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
// A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

// Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

// Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.



char* removeOuterParentheses(char* s) {
    int len = strlen(s);
    int depth = 0, idx = 0;

    printf("Original string: %s\n", s);

    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            if (depth > 0) {
                s[idx++] = s[i];
            }
            depth++;
            printf("Encountered '(': depth = %d, idx = %d, s = %s\n", depth, idx, s);
        } else if (s[i] == ')') {
            depth--;
            if (depth > 0) {
                s[idx++] = s[i];
            }
            printf("Encountered ')': depth = %d, idx = %d, s = %s\n", depth, idx, s);
        }
    }

    s[idx] = '\0'; 
    printf("Modified string: %s\n", s);

    return s;
}


int main () {
    char input[] = "(()())(())";
    removeOuterParentheses(input);
    return 0;
}

