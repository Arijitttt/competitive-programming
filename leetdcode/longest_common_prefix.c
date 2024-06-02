#include<stdio.h>
#include<string.h>
int main(){
	char *str[] = {"flower","flow","flight"};
	int len = sizeof(str)/sizeof(str[0]);
	int b[len];
	int k,i,j,f=0;
	for(i=0;i<len;i++){
		for(j=0;str[i][j]!='\0';j++){
			printf("%c ",str[i][j]); //all elements are being printed

		}
	}
	for(i=0;str[0][i]!='\0';i++){
		for(j=0;str[1][j]!='\0';j++){
			for(k=0;str[2][k]!='\0';k++){
				if(str[0][i]==str[1][j]==str[2][k]){
					//not solved
				}
			}
		}	
	}
	
}
