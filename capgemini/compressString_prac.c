#include<stdio.h>
#include<string.h>
void compressString(char *input){
	int len = strlen(input);
	int count,i;
	for (i=0;i<len;i++){
		printf("%c",input[i]);
		count = 1;
		
		while(i+1<len && input[i]==input[i+1]){
			i++;
			count++;
		}
		if(count>1){
			printf("%d",count);
		}
	}
}
int main(){
	char input[] = "aabbcc";
	compressString(input);
	return 0;
}
