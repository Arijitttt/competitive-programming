#include <stdio.h>
void average_of_multiples(int n,int p){
	int i,sum = 0;
	for (i=0;i<p;i++){
		sum =sum + (n*i);
	}
	int avg = sum / p;
	printf("%d",avg);
}
int main(){
	int n = 6,p = 5;
	average_of_multiples(n,p);
}
