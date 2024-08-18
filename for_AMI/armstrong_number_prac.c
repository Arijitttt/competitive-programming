#include <stdio.h>
#include <math.h>
int armstrong_number(int num){
	int d,t,s=0,i,p;
	p = num;
	while(num>0){
		d = d+1;
		num = num /10;
	}
	num =p;
	while(num>0){
		t = num %10;
		s = s+pow(t,d);
		num=num/10;
	}
	return s;
}
int main(){
	int n = 153;
	int res = armstrong_number(n);
	if(n==res){
		printf("yes");
	}
	else{
		printf("no");
	}
	return 0;
}
