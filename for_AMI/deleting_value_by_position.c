#include <stdio.h>
int deleting_value_by_position(int arr[],int n,int p){
	int i;
	p = p-1;
	if(p>=0 && p<n){
		for(i=p;i<n-1;i++){
			arr[i] = arr[i+1];
		}
		n--;
	}
	
	printf("list is:\n");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	return 0;
}
int main(){
	int arr[] = {3,11,55,77,88,33};
	int n = sizeof(arr)/sizeof(arr[0]);
	int p = 3;
	deleting_value_by_position(arr,n,p);
}

