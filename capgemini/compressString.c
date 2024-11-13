#include <stdio.h>
#include <string.h>
void compressString(char *input){
	int len = strlen(input);
	int count;
	int i;
	for(i=0;i<len;i++){
		printf("%c",input[i]);
		count = 1;
		
		while(i+1<len && input[i] == input[i+1]){
			count++;
			i++;
		}
		if(count > 1){
			printf("%d",count);
		}
	}
}
int main(){
	char input[] ="aabbbbeeeeffggg";
	compressString(input);
}
