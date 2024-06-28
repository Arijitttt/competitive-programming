#include<stdio.h>
void merging_arrays(int a[],int b[],int c[],int len_a,int len_b,int len_c){
	
	int i;
	for(i=0;i<len_a;i++){
		c[i]=a[i];
	}
	int k=len_a;
//	if(len_a>len_b){
//		k=len_a;
//	}
//	else{
//		k=len_b;
//	}
	for(i=0;i<len_b;i++){
		c[k]=b[i];
		k++;
	}
	printf("\n after merging the arrays\n");
	for(i=0;i<len_c;i++){
		printf("%d ",c[i]);
	}
}
after_sorting(int c[],int len_c){
	int i,j,t;
	for(i=0;i<len_c;i++){
		for(j=i+1;j<len_c;j++){
			if(c[i]>c[j]){
				t=c[i];
				c[i]=c[j];
				c[j]=t;
			}
		}
	}
	printf("\nafter sorting\n");
	for(i=0;i<len_c;i++){
		printf("%d ",c[i]);
	}
}
int main(){
	
	
	int a[]={3,2,1,5,2,6,7,8};
	int b[]={90,66,11,33,11,77,9,21};
	int c[100];
	int len_a =sizeof(a)/sizeof(a[0]);
	int len_b =sizeof(b)/sizeof(b[0]);
	int len_c = len_a+len_b;
	merging_arrays(a,b,c,len_a,len_b,len_c);
	after_sorting(c,len_c);



}
