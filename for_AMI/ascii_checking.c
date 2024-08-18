#include <stdio.h>
#include <string.h>
int main(){
	char str[10];
	gets(str);
	if(str[0]==97){
		printf("yes");
	}
	else{
		printf("no");
	}
}
