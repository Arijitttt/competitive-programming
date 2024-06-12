#include<stdio.h>
#include<string.h>

int suffle(char *str1, char *str2, char *result){
    int len1, len2, result_len;
    len1 = strlen(str1);
    len2 = strlen(str2);
    result_len = strlen(result);
    
    if(len1 + len2 != result_len){
        return 0;
    }
    
    int i=0, j=0, k=0;
    
    while(k < result_len){
        if(i < len1 && str1[i] == result[k]){
            i++;
        }
        else if(j < len2 && str2[j] == result[k]){
            j++;
        }
        else{
            return 0;
        }
        k++;
    }
    return 1;
}

int main(){
    char str1[50], str2[50], result[100];
    printf("Enter 1st string: ");
    fgets(str1, 50, stdin);
    str1[strlen(str1) - 1] = '\0'; // remove the newline character
    
    printf("\nEnter 2nd string: ");
    fgets(str2, 50, stdin);
    str2[strlen(str2) - 1] = '\0'; // remove the newline character
    
    printf("\nEnter result string: ");
    fgets(result, 100, stdin);
    result[strlen(result) - 1] = '\0'; // remove the newline character
    
    if(suffle(str1, str2, result)){
        printf("shuffling");
    }
    else{
        printf("not");
    }
    
    return 0;
}
