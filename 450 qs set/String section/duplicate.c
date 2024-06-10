#include<stdio.h>
#include<string.h>
int main(){
	char str[100];
	gets(str);
	int i,j;
	
	for(i=0;str[i]!='\0';i++){
		for(j=i+1;str[j]!='\0';j++){
			if(str[i]==str[j]){
				printf("%c ",str[i]);
			}
		}
		printf("\n");
	}
}
