//count negative days
#include<stdio.h>
int main(){
	int n,i,count=0;
	int arr[10];
	printf("Enter number of days: ");
	scanf("%d",&n);
	printf("\nenter number of prices: ");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	for(i=1;i<n;i++){
		if(arr[i]<arr[i-1]){
			count++;
		}
	}
	printf("%d",count);
}
