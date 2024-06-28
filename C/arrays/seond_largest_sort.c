#include<stdio.h>
void sorted_array(int arr[],int len){
	int i,j,t;
	for(i=0;i<len;i++){
		for(j=i+1;j<len;j++){
			if(arr[i]<arr[j]){
				t=arr[i];
				arr[i]=arr[j];
				arr[j]=t;
			}
		}
	}
}
int second_largest(int arr[],int len,int k){
	return arr[k-1];
}
int main(){
	int arr[]={22,33,11,44,66};
	int len = sizeof(arr)/sizeof(arr[0]);
	sorted_array(arr,len);
	int k=2;
	printf("Second largest element will be : %d",second_largest(arr,len,k));
}
