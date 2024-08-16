#include <stdio.h>
int addition_of_digits(int x){
	int s=0,t;
	while(x>0){
		t = x%10;
		s = s+t;
		x = x/10;
		
	}
	return s;
}
int main(){
	int x = 571,s;
	s = addition_of_digits(x);
	printf("addition : %d",s);
}
