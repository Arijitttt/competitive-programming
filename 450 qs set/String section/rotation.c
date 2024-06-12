#include <stdio.h>
#include <string.h>

int areRotations(char* s1, char* s2) {
    int len1 = strlen(s1);
    int len2 = strlen(s2);

    if (len1 != len2) {
        return 0; // Strings are not rotations of each other
    }

    char temp[len1 * 2];
    strcpy(temp, s1);
    strcat(temp, s1);
    

    if (strstr(temp, s2) != NULL) {
        return 1; // Strings are rotations of each other
    }

    return 0; // Strings are not rotations of each other
}

int main() {
    char s1[100], s2[100];

    printf("Enter the first string: ");
    scanf("%s", s1);

    printf("Enter the second string: ");
    scanf("%s", s2);

    if (areRotations(s1, s2)) {
        printf("Strings are rotations of each other\n");
    } else {
        printf("Strings are not rotations of each other\n");
    }

    return 0;
}
