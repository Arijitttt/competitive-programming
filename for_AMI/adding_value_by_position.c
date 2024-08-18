#include <stdio.h>
int adding_value_by_position(int arr[],int n,int p,int v){
	int i;
	p = p-1;
	if(p>=0 && p<n){
		for(i=n;i>p;i--){
			arr[i] = arr[i-1];
		}
		arr[p] = v;
		n++;
	}
	printf("\nlist is\n");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	return 0;
	
}
int main(){
	int arr[] = {3,11,55,77,88,33};
	int n = sizeof(arr)/sizeof(arr[0]);
	int p = 3;
	int v = 100;
	adding_value_by_position(arr,n,p,v);
}
