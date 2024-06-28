#include<stdio.h>
int main(){
	int arr[] = {22,11,66,54,59,87,43,22,11,22};
	int length = sizeof(arr)/sizeof(arr[0]);
	int i,j,c=0;
	for(i=0;i<length;i++){
		for(j=i+1;j<length;j++){
			if(arr[i]==arr[j]){
				printf("the duplicate is %d\n",arr[j]);
				c++;
			}
		}
	}
	printf("No of duplicate elements: %d",c);
}
