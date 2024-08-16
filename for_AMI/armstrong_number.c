#include <stdio.h>
#include <math.h>
int armstrong_number(int n){
	int p,d,t,s=0;
	p = n;
	while(n>0){
		d = d+1;
		n = n/10;
	}
	n = p;
	while(n>0){
		t = n%10;
		s = s + pow(t,d);
		n = n/10;
	}
	return s;
}
int main(){
	int res,n = 1634;
	res = armstrong_number(n);
	if(res == n){
		printf("%d is a armstrong number",res);
	}
	else{
		printf("not");
	}
}
