#include<stdio.h>
void reverseArray(int a[],int len){
	 int i, temp;
	for(i=0;i<len/2;i++){
		temp = a[i];
		a[i] = a[len-i-1];
		a[len-i-1]= temp;
	}
	for(i=0;i<len;i++){
		printf("%d ",a[i]);
	}
}
int main(){
	int a[] = {1,2,3,4,5,6};
	int len = sizeof(a)/sizeof(a[0]);
	reverseArray(a,len);
}
