#include<stdio.h>
#include<string.h>
int main(){
	char a[100],s[100],c[100];
	gets(s);
	int i,k,j;
	strcpy(a,s);
	strrev(s);
	
	//puts(s);
	
//	for(i=0;s[i]!='\0';i++){
//		for(j=;a[j]!='\0';j++){
//			if(s[i]==a[j]){
//				printf("\nmatching\n");
//				c++;
//			}
//		}
//	}


	for(i=0,j=strlen(a)-1;i<j;i++,j--){
		if(a[i]!=a[j]){
			for(k=j;a[k]!='\0';k++){
				a[k]=a[k+1];
			}
			//c[i]=a[i];
		}
	}
	puts(c);
//	

	//printf("%d",c);
	//puts(a);
	
	
}


//not solved yet properly
