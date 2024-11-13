//second largest
#include<stdio.h>
#include<limits.h>
int second_largest(int arr[],int n){
	int large = INT_MIN;
	int second_large = INT_MIN;
	int i;
	for(i=0;i<n;i++){
		if(arr[i]>large){
			second_large = large;
			large = arr[i];
		}
		else if(arr[i]>second_large && arr[i]!= large){
			second_large = arr[i];
		}
	}
	if(second_large == INT_MIN){
		return -1;
	}
	return second_large;
}
int main(){
	int arr[] = {44,22,33,66,77,11,22};
	int n = sizeof(arr)/sizeof(arr[0]);
	int second_large = second_largest(arr,n);
	printf("%d",second_large);
	return 0;
}
