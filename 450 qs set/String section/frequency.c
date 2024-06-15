#include <stdio.h>
#include <string.h>

void findCharFrequency(const char *C) {
    int freq[256] = {0}; // Assuming ASCII characters
	int i;
    // Calculate frequency of each character in C
    for ( i = 0; i < strlen(C); i++) {
        freq[(int)C[i]]++;
    }

    // Print frequencies of characters
    printf("Character frequencies:\n");
    for ( i = 0; i < 256; i++) {
        if (freq[i] > 0) {
            printf("'%c' : %d\n", (char)i, freq[i]);
        }
    }
}

int main() {
    const char *C = "Hello, World!";
    findCharFrequency(C);
    return 0;
}

