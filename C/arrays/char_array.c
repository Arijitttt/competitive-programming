#include<stdio.h>
#include<string.h>
int main(){
	char a[6];
	int i;
	for (i=0;i<6;i++){
		scanf("%c",&a[i]);
		fflush(stdin);
	}
	printf("\nprint\n");
	for (i=0;i<6;i++){
		printf("%c ",a[i]);
	}
}
