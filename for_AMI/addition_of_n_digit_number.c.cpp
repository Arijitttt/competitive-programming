#include <stdio.h>
int addition_of_n_digit_number(int n){
	int t,s=0;
	while(n>0){
		t =n%10;
		s=s+t;
		n = n/10;
	}
	return s;
}
int main(){
	int x,n=76;
	 x = addition_of_n_digit_number(n);
	 printf("Addition = %d",x);
	 return 0;
}

