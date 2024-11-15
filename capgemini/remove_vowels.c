//remove_vowels
#include<stdio.h>
#include<string.h>
#include<ctype.h>
int isVowel(char ch){
	ch = tolower(ch);
	return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
}
void removeVowels(char str[]){
	int i,j=0;
	for(i=0;i<strlen(str);i++){
		if(!isVowel(str[i])){
			str[j++] = str[i];
		}
	}
	str[j] = '\0';
}
int main() {
	char str[100];
	printf("Enter a string: ");
	fgets(str,sizeof(str),stdin);
	str[strcspn(str,"\n")] = '\0';
	removeVowels(str);
	printf("%s",str);
}
