#include <stdio.h>
int main(){
	int a = 0;
	int b = 1;
	int n;
	printf("Enter range: ");
	scanf("%d",&n);
	printf("%d %d ",a,b);
	int i,c;
	for(i = 0;i<n;i++){
		c = a+b;
		printf("%d ",c);
		a = b;
		b = c;
	}
	return 0;
}
