#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>


int main() {
    __uint128_t number = 112312123112313ULL;
    float fnumber = 1.35;
    bool isGustavoHandsome = false;
    // printf("Number: %llu%llu\n",
    //     (unsigned long long)(number >> 64), // High 64 bits
    //     (unsigned long long)(number & 0xFFFFFFFFFFFFFFFFULL)); // Low 64 bits
    uint8_t a = 12;
    uint8_t b = 5;
    printf("shifing to the right %u\n", a >> 1);
    printf("shifing to the left %u\n", b << 1);

    return 0;
}


