#include<stdio.h>
#include<string.h>
int main(){
	char a[100],b[100];
	int i,j,t;
	printf("Enter 1st String : ");
	gets(a);
	printf("Enter 2nd String : ");
	gets(b);
	if(strlen(a) != strlen(b)){
		printf("Not an anagram string at all !");
		
	}
	for(i=0;i<strlen(a);i++){
		for(j=i+1;j<strlen(b);j++){
			if(a[i]>a[j]){
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
			if(b[i]>b[j]){
				t=b[i];
				b[i]=b[j];
				b[j]=t;
			}
		}
	}
	if(strcmp(a,b) == 0){
		printf("it is a anagram string");
	}
	else{
		printf("not a anagram string");
	}
}
