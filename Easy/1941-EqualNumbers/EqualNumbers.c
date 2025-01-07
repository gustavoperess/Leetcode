
#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
// Given a string s, return true if s is a good string, or false otherwise.
// A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

// Example 1:

// Input: s = "abacbc"
// Output: true
// Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
// Example 2:

// Input: s = "aaabb"
// Output: false
// Explanation: The characters that appear in s are 'a' and 'b'.
// 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

bool areOccurrencesEqual(char *s)
{
    int freq[26] = {0};

    for (int i = 0; s[i] != '\0'; i++)
    {
        if(isalpha(s[i])) 
        {
            char lowerChar = tolower(s[i]);
            freq[lowerChar - 'a']++;
        }
     
    }
    int t = freq[s[0]-'a'];
    for (int i = 0; i < 26; i ++) 
    {
     if (freq[i] > 0) 
        {
            if(freq[i] != t) {
                return false;
            }
        }
    }

    return true;
}

int main()
{
    char input[] = "aabbccdd";
    areOccurrencesEqual(input);
    return 0;
}
