#include <stdio.h>

int main() {
    // Increased the size of array by 1 to accommodate the new element
    int a[8] = {11, 22, 44, 33, 55, 88, 22};
    int i, p, v;
    int len = sizeof(a) / sizeof(a[0]) - 1; 
    
    printf("Original array length: %d\n", len);
    printf("The array list is: \n");
    for (i = 0; i < len; i++) {
        printf("%d ", a[i]);
    }
    printf("\nEnter the position you want to insert your required value: ");
    scanf("%d", &p);
    p -= 1; 
    
    if (p >= 0 && p <= len) {
        printf("Enter your value: ");
        scanf("%d", &v); 

        
        for (i = len; i > p; i--) {
            a[i] = a[i - 1];
        }
        a[p] = v; 
        len++; 

        printf("New list is: ");
        for (i = 0; i < len; i++) {
            printf("%d ", a[i]);
        }
    } else {
        printf("Array index out of bounds");
    }

    return 0;
}

