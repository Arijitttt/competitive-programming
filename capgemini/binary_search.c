#include<stdio.h>
int main(){
	int arr[100];
	int j,i,t,n = 5,target;
	printf("enter target element: ");
	scanf("%d",&target);
	printf("enter elements for arr\n");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	//sorting
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if(arr[i]>arr[j]){
				t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}
	int low = 0;
	int high = n-1;
	while (low<high){
		int mid = (low+high)/2;
		if(arr[mid] == target){
			printf("index : %d",mid);
			break;
		}
		else if(arr[mid] > target){
			high = mid -1;
		}
		else{
			low = mid+1;
		}
	}
}
