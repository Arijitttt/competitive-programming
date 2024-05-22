#include<stdio.h>
int main(){
	int a[6];
	int n=10,i;
	a[0] = 0;
	a[1] = 1;
	printf("Fibonacci  :-");
	for(i=2;i<n;i++){
		a[i] = a[i-2]+ a[i-1];
	}
	for(i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
