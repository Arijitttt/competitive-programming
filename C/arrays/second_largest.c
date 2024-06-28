#include<stdio.h>
int sec_largest(int a[],int len,int m,int n){
	int i;
	for(i=0;i<len;i++){
		if(m<a[i]){
			n=m;
			m=a[i];
		}
		else if(n<a[i] && a[i]!=m){
			n = a[i];
		}
		
	}
	if(m == n){
		return 0;
	}
	else{
		return n;
	}
}
int main(){
	int arr[]={22,33,11,66,44,66};
	int len = sizeof(arr)/sizeof(arr[0]);
	int m = arr[0];
	int n = arr[0];
	printf("Second largest element will be : %d",sec_largest(arr,len,m,n));
}
