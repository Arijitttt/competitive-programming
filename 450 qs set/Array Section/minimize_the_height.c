#include<stdio.h>

void minimizing_height(int a[], int len, int k) {
    int i, max, min;

    // Find the maximum and minimum values in the array
    max = min = a[0];
    for(i = 1; i < len; i++) {
        if(a[i] > max) {
            max = a[i];
        }
        if(a[i] < min) {
            min = a[i];
        }
    }

    // Calculate the minimum possible difference
    int diff1 = max - k - (min + k);
    int diff2 = (max - k) - (min + k);
    int min_diff = (diff1 < diff2) ? diff1 : diff2;

    printf("Minimum possible difference: %d\n", min_diff);

    // Modify the array
    for(i = 0; i < len; i++) {
        if(a[i] == max) {
            a[i] -= k;
        } else {
            a[i] += k;
        }
    }

    // Print the modified array
    for(i = 0; i < len; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main() {
    int a[] = {3, 9, 12, 16, 20};
    int len = sizeof(a) / sizeof(a[0]);
    int k = 3;

    minimizing_height(a, len, k);

    return 0;
}
