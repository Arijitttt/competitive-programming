#include<stdio.h>
void sort(int a[],int len){
	int t,i,j;
	for(i=0;i<len;i++){
		for(j=i+1;j<len;j++){
			if(a[i]>a[j]){
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
		}
		//test
		printf("%d ",a[i]);
	}
	printf("\n");
}
int main(){
	int arr[]={0,2,1,2,0};
	int len = sizeof(arr)/sizeof(arr[0]);
	sort(arr,len);
}
