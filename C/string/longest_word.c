#include<stdio.h>
#include<string.h>
int main(){
	char a[100],b[100],c[100];
	int i,j,m=0;
	
	gets(a);
	
	for(i=0,j=0;a[i]!='\0';i++){
		if(a[i]!=' '){
			b[j]=a[i];
			j++;
		}
		else{
			b[j]='\0';
			j=0;
			if(strlen(b)>m){
				m=strlen(b);
				strcpy(c,b);
			}
		}
	}
	
	puts(c);
	
	return 0;
}
