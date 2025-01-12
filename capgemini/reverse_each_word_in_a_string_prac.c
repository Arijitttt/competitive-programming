#include<stdio.h>
#include<string.h>
void reverseEachWord(char *str,int start,int end){
	char t;
	while(start<end){
		t =str[start];
		str[start] = str[end];
		str[end] = t;
		start++;
		end--;
	}
}
void reverseWord(char *str){
	int start = 0,end = 0,length = strlen(str);
	while(end <=length){
		if(str[end] == ' ' || str[end] == '\0'){
			reverseEachWord(str,start,end-1);
			start = end +1;
		}
		end++;
	}
}
int main(){
	char input[100];
	printf("Enter a string: ");
	fgets(input,sizeof(input),stdin);
	input[strcspn(input,"\n")] = '\0';
	reverseWord(input);
	printf("%s",input);
}
