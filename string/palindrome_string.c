#include<stdio.h>
#include<string.h>
int main(){
	char a[20],b[20];
	printf("Enter a string to check palindrome...\n");
	gets(a);
	strcpy(b,a);
	strrev(b);
	if(strcmp(a,b) == 0){
		puts(a);
		printf("is a palindrome string");
	}
	else{
		printf("Not a palindrome string");
	}
	return 0;
}
