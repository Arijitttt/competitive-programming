#include<stdio.h>
#include<string.h>
int main() {
	char s[100];
	gets(s);
    int k,i,j,c;
    
    for(i=0;s[i]!='\0';i++){
    	c=1;
        for(j=i+1;s[j]!='\0';j++){
            if(s[i]==s[j]){
                c++;
                s[j] = '\0';
                
                
                for(k=j;s[k]!='\0';k++){
                	s[k]=s[k+1];
                	
				}
                
                
            }
        }
        
       
    }
    int len = strlen(s);
    printf("%d",len);
    
}
