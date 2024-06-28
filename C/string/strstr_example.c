#include<stdio.h>
#include<string.h>
int main(){
	char str[]="hello world";
	char sub_str[]="world";
	char *result = strstr(str,sub_str);
	if(result != NULL){
		printf("found %s in %s\n",sub_str,str);
		printf("The rest of the string is %s",result);
	}
	else{
		printf("not found");
	}
}
