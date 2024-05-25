#include<stdio.h>
#include<string.h>
int main(){
	char a[20],b[20],c[20],d[20];
	printf("Enter a string: ");
	gets(a);
	printf("%d\n",strlen(a));
	int i;
	for(i=0;a[i]!='\0';i++);
	printf("%d",i);
	strcpy(b,a);
	puts(b);
	strcat(a,b);
	puts(a);
	
	printf("Enter one string for strcmp: ");
	gets(c);
	printf("Enter another string for strcmp: ");
	gets(d);
	printf("%d",strcmp(c,d));
}
