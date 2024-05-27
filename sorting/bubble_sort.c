#include<stdio.h>
int main(){
	int a[5] = {3,5,1,2,6};
	int i,j,t;
	int len = sizeof(a)/sizeof(a[0]);
	
	for(i=0;i<len;i++){
		for(j=0;j<len-i-1;j++){
			if(a[j]>a[j+1]){
				t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
			}
		}
	}
	printf("Ater bubble sort\n");
	for(i=0;i<len;i++){\
		printf("%d ",a[i]);
	}
}
