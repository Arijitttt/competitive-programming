//swap without using 3rd variable
#include<stdio.h>
int main(){
	int a,b;
	printf("Enter a & b: ");
	scanf("%d%d",&a,&b);
	a = a+b;
	b = a-b;
	a= a-b;
	printf("%d %d",a,b);
}
