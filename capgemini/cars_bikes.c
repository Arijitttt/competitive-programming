//cars_bikes
#include<stdio.h>
int main(){
	int t;
	scanf("%d",&t);
	int i;
	for(i=0;i<t;i++){
		int c,b,s=0;
		scanf("%d%d",&c,&b);
		s = (c*4)+(b*2);
		printf("%d",s);
	}
}
