#include <stdio.h>
int remove_index(int arr[],int n,int p){
	int i;
	if(p>=0 && p<n){
			for(i=p;i<n;i++){
				arr[i] = arr[i+1];
		}
		n--;
	}
	return n;
	
}
int main(){
	int arr[] = {33,55,44,11,88};
	int i;
	int n = sizeof(arr)/sizeof(arr[0]);
	int p = 2;
	n = remove_index(arr,n,p);
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
}
