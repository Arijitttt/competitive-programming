#include<stdio.h>
void sorted_array(int a[],int len){
	int i,j,t;
	for(i=0;i<len;i++){
		for(j=i+1;j<len;j++){
			if(a[i]>a[j]){
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
		}
	}
	
}
void arraydisect(int a[], int len){
    int i, j1 = 0, j2 = 0;
    int b[len], c[len];
	for(i=0;i<len;i++){
		if(a[i]<0){
			b[j1]=a[i];
			j1++;
		}
		else{
			c[j2] = a[i];
			j2++;
		}
	}
	for(i=0;i<j1;i++){
		printf("%d ",b[i]);
	}
	printf("\n");
	for(i=0;i<j2;i++){
		printf("%d ",c[i]);
	}
}
int main(){
	int a[]={-12, 11, -13, -5, 6, -7, 5, -3, -6};
	int len = sizeof(a)/sizeof(a[0]);
	sorted_array(a,len);
	arraydisect(a,len);
}
