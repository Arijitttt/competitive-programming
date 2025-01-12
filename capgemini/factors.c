//factors
#include<stdio.h>
int main(){
	int n,i,j=0;
	int temp[100];
	printf("Enter number: ");
	scanf("%d",&n);
	if(n==0){
		printf("\nno factors");
		
	}
	else{
		for(i=1;i<=n;i++){
			if(n%i == 0){
				printf("%d ",i);
				temp[j++] = i;
			}
		}
	}
	printf("array is ");
	for(i=0;i<j;i++){
		printf("%d ",temp[i]);
	}
	return 0;
}
