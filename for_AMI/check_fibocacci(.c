#include <stdio.h>
int check_fibocacci(int x){
	int s=0,t;
	while(x>0){
		t = x%10;
		s = s*10+t;
		x = x/10;
	}
	return s;
}
int main(){
	int x=23,s;
	s = check_fibocacci(x);
	if(x == s){
		printf("fibonacci number");
	}
	else{
		printf("Not");
	}
	
}
