#include <stdio.h>
#include <string.h>

void longestPalindrome(char str[]) {
    int n = strlen(str);
    int max = 1, start = 0;
    int i,j,k,flag;

    for ( i = 0; i < strlen(str); i++) {
        for ( j = i; j < strlen(str); j++) {
            flag = 1;

            for ( k = 0; k < (j - i + 1) / 2; k++)
                if (str[i + k] != str[j - k])
                    flag = 0;

            if (flag && (j - i + 1) > max) {
                start = i;
                max = j - i + 1;
            }
        }
    }

    for ( i = start; i <= start + max - 1; ++i)
        printf("%c", str[i]);
}

int main() {
    char str[] = "abba";
    longestPalindrome(str);
    return 0;
}

