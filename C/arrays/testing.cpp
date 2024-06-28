#include<stdio.h>
int main(){
	int arr[10];
	int i,n;
	printf("Enter the range: ");
	scanf("%d",&n);
	for(i=0;i<n;i++){
		printf("Enter the elements of the array: ");
		scanf("%d",&arr[i]);		
	}
	printf("Array is: ");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	return 0;
}
