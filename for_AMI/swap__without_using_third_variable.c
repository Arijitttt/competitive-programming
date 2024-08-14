#include <stdio.h>
void swap__without_using_third_variable(int x,int y){
	x = x+y;
	y = x-y;
	x = x-y;
	printf("Swapped value: %d,%d",x,y); 
}
int main(){
	int x,y;
	printf("two integer: ");
	scanf("%d%d",&x,&y);
	swap__without_using_third_variable(x,y);
	return 0;
	
}
