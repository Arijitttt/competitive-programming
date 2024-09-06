#include <stdio.h>
void sum_of_vowels(n){
	int i,sum = 0;
	for(i=2;i<=n;i+=2){
		if(i%2==0){
			sum = sum + i;
		}
	}
	printf("%d",sum);
}
int main(){
	sum_of_vowels(6);
}

