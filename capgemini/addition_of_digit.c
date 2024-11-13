//addition of 3 digit number
#include <stdio.h>
int main(){
	int a,t,s=0;
	scanf("%d",&a);
	while(a>0){
		t = a%10;
		s= s+t;
		a =a/10;
	}
		
	printf("%d",s);
}
