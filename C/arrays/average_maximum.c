#include<stdio.h>
int main(){
	int a[10];
	int i,s=0,n = 10,max;
	float avg;
	printf("Enter values for array: ");
	for(i = 0 ; i<n;i++){
		scanf("%d",&a[i]);
		s+=a[i];
	}
	
	int length = sizeof(a)/sizeof(a[0]);
	avg = (float)s/length;
	printf("Avg = %f",avg);
	max = a[0];
	for(i = 0 ; i<n;i++){
		if(a[i]>max){
			max= a[i];
		}
	}
	printf("Max = %d",max); 	
}
