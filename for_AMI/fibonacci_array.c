#include <stdio.h>
int fibonacci_array(int arr[],int n){
	int i;
	arr[0] = 0;
	arr[1] = 1;
	for(i=2;i<n;i++){
		arr[i] = arr[i-2]+arr[i-1];
	}
	printf("\nfibonacci array: ");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	return 0;
}
int main(){
	int arr[10];
	int n = sizeof(arr)/sizeof(arr[0]);
	fibonacci_array(arr,n);
}
