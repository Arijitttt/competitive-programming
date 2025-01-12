#include<stdio.h>
#include<string.h>
int main(){
	int n,i;
	printf("enter no of products:  ");
	scanf("%d",&n);
	char min_product[100];
	int min_discount = 101;
	for(i=0;i<n;i++){
		char name[100];
		int price,discount;
		printf("\nEnter product name,price and discount:");
		scanf("%s %d %d",name, &price, &discount);
		
		if(discount<min_discount){
			min_discount = discount;
			strcpy(min_product,name);
		}
	}
	printf("Product with minimun discount : %s",min_product);
}
