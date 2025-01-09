#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int numJewelsInStones(char *jewels, char *stones)
{
    int list[123] = {0};
    int count = 0;

    while (*jewels) {
        list[*jewels++]++;
    }
    while (*stones) {
        count += list[*stones++];
    }

    return count;
}

int main()
{
    numJewelsInStones("aA", "aAAbbbb");
    return 0;
}