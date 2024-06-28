#include<stdio.h>
#include<string.h>
int main(){
	char copy[100],pali[100];
	gets(pali);
	strcpy(copy,pali);
	puts(copy);
	if(strcmp(copy,pali)==0){
		printf("it is a palindrome string");
	}
	else{
		printf("not a palindrome string");
	}
	
}
