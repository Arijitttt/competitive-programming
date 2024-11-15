//longest word
#include<stdio.h>
#include<string.h>
int main(){
	char a[100],b[100],c[100];
	printf("enter a string: ");
	fgets(a,sizeof(a),stdin);
	a[strcspn(a,"\n")] = '\0';
	int i,m=0,j=0;
	for(i=0;i<=strlen(a);i++){
		if(a[i] != ' ' && a[i] != '\0'){
			b[j] = a[i];
			j++;
		}
		else{
			b[j] = '\0';
			j=0;
			if(m<strlen(b)){
				m = strlen(b);
				strcpy(c,b);
				
			}
			
		}
	}
	printf("%s",c);
}
