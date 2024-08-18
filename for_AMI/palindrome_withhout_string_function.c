#include <stdio.h>
#include <string.h>
int isPalindrome(char *str){
    int i, j, n;
    for(n=0; str[n]!= '\0'; n++);
    for(i=0, j=n-2; i<j; i++, j--){
        if(str[i] != str[j]){
            return 0;
        }
    }
    return 1;
}
int main(){
    char str1[50];
    fgets(str1, sizeof(str1), stdin);
    int res = isPalindrome(str1);
    printf("%d",res);
    return 0;
}
