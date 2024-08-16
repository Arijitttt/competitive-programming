#include <stdio.h>
int main(){
	int t,s = 0,n = 89;
	while(n>0){
		t = n%10;
		s = s*10 + t;
		n = n/10;
	}
	printf("reverse : %d",s);
	return 0;
}

