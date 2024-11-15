//camel_case
#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main(){
	char s[100],res[100];
	fgets(s,sizeof(s),stdin);
	s[strcspn(s,"\n")] = '\0';
	int i;
	for(i=0;i<strlen(s);i++){
		if(s[i]>= 'a' && s[i]<='z'){
			res[i] = toupper(s[i]);
		}
		else{
			res[i] = tolower(s[i]);
		}
	}
	res[i] = '\0';
	printf("\n%s",res); 
}
