//largest_element
#include<stdio.h>
int main(){
	int i,m;
	int arr[] = {11,44,33,77,55,33};
	int n = sizeof(arr)/sizeof(arr[0]);
	m = arr[0];
	for(i=0;i<n;i++){
		if (arr[i]>m){
			m =arr[i];
		}
	}
	printf("%d",m);
}
