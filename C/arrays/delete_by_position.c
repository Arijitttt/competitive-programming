#include<stdio.h>
int main(){
	int a[] ={11,44,33,22,11};
	int len = sizeof(a)/sizeof(a[0]);
	//printf("%d",len);
	int i,p;
	printf("Enter position top be deleted: ");
	scanf("%d",&p);
	p-=1;
	if(p>=0 && p<=len){
		for(i=p;i<len;i++){
			a[i] = a[i+1];
			len --;
		}
		for(i=0;i<len;i++){
			printf("%d ",a[i]);
		}
	}
	return 0;
}
