#include <stdio.h>
#include<string.h>
void title_case(char *str){
	int i;
	if(str[0]>=97 && str[0]<=122){
		str[0]-=32;
	}
	for(i=1;str[i]!='\0';i++){
		if(str[i]==' '){
			if(str[i+1]>=97 && str[i+1]<=122){
				str[i+1]-=32;
			}
		}
	}
}
int main(){
	char str[100];
	gets(str);
	title_case(str);
	puts(str);
	return 0;
}
