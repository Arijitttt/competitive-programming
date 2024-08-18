#include <stdio.h>
#include <string.h>
void anagram(char *a,char *b){
	if(strlen(a) != strlen(b)){
		printf("not same length");
	}
	int i,j,t;
	for(i=0;i<strlen(a);i++){
		for(j=i+1;j<strlen(a);j++){
			if(a[i]>a[j]){
				t = a[i];
				a[i] = a[j];
				a[j] = t;
			}
			if(b[i]>b[j]){
				t = b[i];
				b[i] = b[j];
				b[j] = t;
			}
		}
	}
	if(strcmp(a,b) == 0){
		printf("anagram");
	}
	else{
		printf("not");
	}
}
int main(){
	char a[10],b[10];
	gets(a);
	gets(b);
	anagram(a,b);
}
