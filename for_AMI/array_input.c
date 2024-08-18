#include <stdio.h>
int main(){
	int arr[10];
	int i;
	printf("no of elements: ");
	for(i=0;i<5;i++){
		scanf("%d",&arr[i]);
	}
	printf("list is");
	for(i=0;i<10;i++){
		printf("%d ",arr[i]);
	}
	
}
