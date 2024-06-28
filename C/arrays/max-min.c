#include<stdio.h>
int main(){
	int a[5] = {1,2,3,4,6};
	int left = 0;
	int right = 5-1;
	int h = (a[left]<a[right]?a[right] : a[left]);
	printf("Height = %d",h);
}
