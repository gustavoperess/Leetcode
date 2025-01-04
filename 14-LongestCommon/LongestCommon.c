
#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        return ""; 
    }
    int min = strlen(strs[0]);
    for(int i = 0; i < strsSize; i++) {
        int j = 0;
        size_t length = strlen(strs[i]);
        while(j < length && strs[i][j] == strs[0][j]) {
            j++;
        }
         min = (j < min) ? j : min;
    }
    char* prefix = (char*)malloc((min + 1) * sizeof(char));
     if (prefix == NULL) {
        return "";
    }
    strncpy(prefix, strs[0], min);
    prefix[min] = '\0';
    printf("%s\n", prefix);
    return prefix;
}

int main()
{
    char *input[] = {"dog","racecar","car"};
    longestCommonPrefix(input, 3);
    return 0;
}
