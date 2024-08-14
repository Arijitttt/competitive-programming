#include <stdio.h>
int absolute_number(int a){
	if(a<0){
		a = -a;
	}
	return a;
}
int main(){
	int x,y;
	printf("Enter a no: ");
	scanf("%d",&x);
	y = absolute_number(x);
	printf("absolute value: %d",y);
	return 0;
}
