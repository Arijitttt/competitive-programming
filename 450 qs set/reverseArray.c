#include<stdio.h>
void reverseArray(int a[],int length){
	int i,j;
	int b[length];
	for(i=length-1,j=0;i>=0;i--,j++){
		b[j]=a[i];
		
	}
	for(i=0;i<length;i++){
		printf("%d ",b[i]);
	}
}
int main(){
	int arr[]= {11,22,33,55,66};
	int length=sizeof(arr)/sizeof(arr[0]);
	printf("%d\n",length);
	reverseArray(arr,length);
}

//time complexity = O(log n)
