#include <stdio.h>
#include <string.h>
void remove_vowel(char *s){
	int n = strlen(s);
	int i,j;
	for(i=0;i<n;i++){
		if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i]== 'o' || s[i]=='u'){
			for(j = i;j<n;j++){
				s[j]  = s[j+1];
			}
			n--;
			i--;
		}
		s[n] = '\0';
	}
}
int main(){
	char s[] = "gag";
	remove_vowel(s);
	printf("%s",s);
	return 0;
}
	


