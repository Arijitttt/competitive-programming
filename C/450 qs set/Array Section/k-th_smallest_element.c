#include<stdio.h>
void sorting_array(int a[],int len){
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
int k_smallestElement(int a[],int len,int m,int k){
//		int i;
//		for(i=0;i<len;i++){
//			if(a[i]<m){
//				m=a[i];
//			}
//		}
		return a[k-1];
}
int main(){
	int a[]={11,66,44,33,22};
	int len =sizeof(a)/sizeof(a[0]);
	sorting_array(a,len);
	int m = a[0];
	int k;
	printf("Position: ");
	scanf("%d",&k);
	printf("K-th smallest element = %d",k_smallestElement(a,len,m,k));
	
}
