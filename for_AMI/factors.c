#include <stdio.h>
int main(){
	int i,n;
	printf("Enter range: ");
	scanf("%d",&n);
	for(i=1;i<n;i++){
		if(n%i==0){
			printf("%d ",i);
		}
	}
}
