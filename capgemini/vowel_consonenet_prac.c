#include<stdio.h>
#include<string.h>
#include<ctype.h>
int isVowel(char ch){
	ch = tolower(ch);
	return(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}
void replaceVowel(char str[]){
	int i;
	for(i=0;i<strlen(str);i++){
		if(isVowel(str[i])){
			str[i] = '.';
		}
	}
}
int main(){
	char str[100];
	fgets(str,sizeof(str),stdin);
	str[strcspn(str,"\n")]= '\0';
	replaceVowel(str);
	printf("%s",str);
}
