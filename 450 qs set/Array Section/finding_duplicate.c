#include<stdio.h>
int main(){
	int a[]={1,4,4,3,2};
	int len = sizeof(a)/sizeof(a[0]);
	int i,j;
	for(i=0;i<len;i++){
		for(j=i+1;j<len;j++){
			if(a[i]==a[j]){
				printf("%d ",a[j]);
			}
		}
	}
}
