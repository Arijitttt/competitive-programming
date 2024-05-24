//binary search

#include<stdio.h>
int main(){
	int a[] ={11,44,33,77,45};
	int len = sizeof(a)/sizeof(a[0]);
	int i,j,key,low,mid,high,t,f=0;
	printf("before sort\n");
	for(i=0;i<len;i++){
		printf("%d ",a[i]);
	}
	printf("\nafter sort\n");
	for(i=0;i<len;i++){
		for(j = i+1 ; j<len;j++){
			if(a[i]>a[j]){
				t= a[i];
				a[i] = a[j];
				a[j]= t;
			}
		}
	}
	for(i=0;i<len;i++){
		printf("%d ",a[i]);
	}
	printf("\n enter value to be searched\n");
	scanf("%d",&key);
	
	low = 0;
	high = len-1;
	mid = (low+high)/2;
	
	while(low<=high){
		if(a[mid]==key){
			mid++;
			printf("\nposition = %d\n",mid);
			f= 1;
			break;
		}
		else if(a[mid]>key){
			high = mid - 1;
		}
		else if(a[mid]<key){
			high = mid + 1;
		}
		mid = (low+high)/2;
	}
	if(f == 0){
		printf("\nnot found");
	}
	return 0;
	
}
