#include<stdio.h>
#include<string.h>
int main(){
	char a[100];
	int i;
	printf("Enter a string :");
	gets(a);
	if(a[0]>=97 && a[0]<=122){
		a[0] = a[0]-32;
	}
	for(i=1;a[i]!='\0';i++){
		if(a[i] == ' '){
			if(a[i+1] >=97 && a[i+1]<=122){
				a[i+1] = a[i+1] -32;
			}
		}
	}
	puts(a);
}
