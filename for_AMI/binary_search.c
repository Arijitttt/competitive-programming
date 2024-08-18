#include <stdio.h>
void selection_sort(int arr[],int n){
	int j,i,t;
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if(arr[i]>arr[j]){
				t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}
}
int binary_search(int arr[],int n,int target){
	int low,high,mid;
	low = 0;
	high = n-1;
	mid = (low+high)/2;
	while(low<=high){
		if(arr[mid]==target){
			return mid;
		}
		else if(arr[mid]>target){
			high = mid -1;
		}
		else if(arr[mid]<target){
			low = mid +1;
		}
		else{
			return -1;
		}
	}
}
int main(){
	int arr[] = {55,11,22,33,88,22,11};
	int n = sizeof(arr)/sizeof(arr[0]);
	selection_sort(arr,n);
	int i,target = 22;
	int result  = binary_search(arr,n,target);
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	printf("\n index  = %d",result);
	
	return 0;
}
//int binary_search(int arr[]){
//}
