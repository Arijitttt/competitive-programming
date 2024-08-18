#include <stdio.h>
int average_maximum(int arr[],int n){
	int s=0,i,j;
	float avg;
	for(i=0;i<n;i++){
		s= s+arr[i];
	}
	avg = (float)s/n;
	printf("average is %.2f\n",avg);
	int m = arr[0];
	for(i=0;i<n;i++){
		if(m<arr[i]){
			m = arr[i];
		}
	}
	printf("maximum = %d",m);
	return 0;
}
int main(){
	int arr[] = {11,33,44,22,66};
	int n = sizeof(arr)/sizeof(arr[0]);
	average_maximum(arr,n);
}
