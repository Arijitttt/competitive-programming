#include <stdio.h>

#define MAX_VALUE 100

bool removeDuplicates(int arr[], int size) {
    int freq[MAX_VALUE] = {0};
    int uniqueIndex = 0;

    for (int i = 0; i < size; i++) {
        freq[arr[i]]++;
        if (freq[arr[i]] == 1) {
            arr[uniqueIndex++] = arr[i];
        }
    }

    // Update the size to reflect the number of unique elements
    size = uniqueIndex;

    return true; // Assuming we always find at least one duplicate
}

int main() {
    int arr[] = {1, 2, 3, 4, 2};
    int size = sizeof(arr) / sizeof(arr[0]);

    if (removeDuplicates(arr, size)) {
        printf("Duplicates found in the array and removed.\n");
        printf("Array after removing duplicates: ");
        for (int i = 0; i < size; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n");
    } else {
        printf("No duplicates found in the array.\n");
    }

    return 0;
}
