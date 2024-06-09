#include <stdio.h>
#include <limits.h>

int minJumps(int arr[], int n) {
    int jumps[n];
    int i,j;
    for ( i = 0; i < n; i++) {
        jumps[i] = INT_MAX;
        printf("%d ",jumps[i]);
    }
    jumps[0] = 0;

    for (i = 1; i < n; i++) {
        for ( j = 0; j < i; j++) {
            if (j + arr[j] >= i) {
                jumps[i] = (jumps[i] > jumps[j] + 1)? jumps[j] + 1 : jumps[i];
            }
        }
    }

    return (jumps[n - 1] == INT_MAX)? -1 : jumps[n - 1];
}

int main() {
    int arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Minimum number of jumps: %d\n", minJumps(arr, n));
    return 0;
}
