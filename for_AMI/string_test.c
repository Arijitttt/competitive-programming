#include <stdio.h>
#include <string.h>
void string_test(char *str){
	puts(str);
	int i;
	for(i=0;str[i] != '\0';i++);
	printf("Lenghth = %d",i);
	
}
int main(){
	char str[100];
	printf("string: ");
	gets(str);
	string_test(str);
}
