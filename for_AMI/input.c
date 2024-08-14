#include <stdio.h>
int input(){
	int x;
	printf("Enter a integer number: ");
	scanf("%d",&x);
	return x;
}
int main(){
	int a,x;
	a = input();
	printf("%d",a);
}
