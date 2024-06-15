#include<stdio.h>
#include<string.h>
void frequency(char str[]){
	int freq[256]={0};
	int i;
	for(i=0;i<strlen(str);i++){
		freq[(int)str[i]]++;
	}
	printf("frequency:\n");
	//highest frequency
	int m =freq[0]; 
	for(i=0;i<256;i++){
		if(freq[i]>m){
			m=freq[i];
		}
	}
	for(i=0;i<256;i++){
		if(freq[i]==m){
			printf("%c ",i);
		}
	}
	printf("occur %d times.\n", m);
}
int main(){
	char str[]="My name is arijit bhattacharya";
	frequency(str);
	return 0;
}
