#include<stdio.h>
#include<string.h>
void longestPalindrome(char str[]){
	int len = strlen(str);
	int k,i,j,flag=0;
	int start=0,max=1;
	for(i=0;i<len;i++){
		for(j=i;j<len;j++){
			flag = 1;
			
			for(k=0;k<(j-i+1)/2;k++){
				if(str[i+k]!=str[j-k]){
					flag=0;
				}
				
			}
			if(flag && (j-i+1)>max){
				start=i;
				max=j-i+1;
			}
		}
	}
	
	for(i=start;i<start+max-1;++i){
		printf("%c",str[i]);
	}
}
int main(){
	char str[]="abba";
	longestPalindrome(str);
}
