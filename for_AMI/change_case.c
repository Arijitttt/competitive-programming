#include <stdio.h>
int main(){
	char m;
	printf("Enter a charecter: ");
	scanf("%c",&m);
	if(m>=32 && m<=90){
		m+= 32;
		printf("converted: %c",m);
	}
	if(m>=97 && m<=122){
		m-=32;
		printf("converted: %c",m);
	}
}
