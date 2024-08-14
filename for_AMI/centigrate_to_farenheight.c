#include <stdio.h>
int main(){
	float c,f;
	printf("enter temperature in Centigrade: ");
	scanf("%f",&c);
//	f = (9*c + 160) / 5;
	f = (9.0/5.0) * c + 32.0;
	printf("\nfarenheight: %.2f",f);
}
