//anagram
#include<stdio.h>
#include<string.h>
int main(){
	char str1[100],str2[100];
	printf("Enter string 1: ");
	fgets(str1,sizeof(str1),stdin);
	str1[strcspn(str1,"\n")] = '\0';
	printf("\nEnter String 2: ");
	fgets(str2,sizeof(str2),stdin);
	str2[strcspn(str2,"\n")] = '\0';
	int i , j ,t;
	if(strlen(str1) != strlen(str2)){
		printf("not anagram");
	}
	else{
		for(i=0;i<strlen(str1);i++){
			for(j=i+1;j<strlen(str1);j++){
				if(str1[i]>str1[j]){
					t = str1[i];
					str1[i] = str1[j];
					str1[j] = t;
				}
				if(str2[i]>str2[j]){
					t = str2[i];
					str2[i] = str2[j];
					str2[j] = t;
				}
			}
		}
	}
	
	if(strcmp(str1,str2) == 0){
		printf("anagram");
	}
	else{
		printf("not anagram");
	}
}
