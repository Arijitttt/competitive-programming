#include<stdio.h>
#include<string.h>

int main(){
	int rev=0,reminder,n=513;
	while(n>0){
		reminder = n%10;
		rev = rev*10 + reminder;
		n = n/10;
	}
	printf("%d",rev);
}



//int main(){
//	int a[]={1,2,3};
//	int i,j=0,t;
//	int len = 3;
//	int rev[len];
//	
//	for(i=len-1;i>=0;i--){
//		rev[j] = a[i];
//		j++;
//	}
//	for(i=0;i<len;i++){
//		printf("%d ",rev[i]);
//	}
//}



//#include<stdio.h>  
//int main()  
//{  
//    int n, arr[n], i;  
//    printf("Enter the size of the array: ");  
//    scanf("%d", &n);  
//    printf("Enter the elements: ");  
//    for(i = 0; i < n; i++)  
//    {  
//        scanf("%d", &arr[i]);  
//    }  
//    int rev[n], j = 0;  
//    for(i = n-1; i >= 0; i--)  
//    {  
//        rev[j] = arr[i];  
//        j++;  
//    }  
//    printf("The Reversed array: ");  
//    for(i = 0; i < n; i++)  
//    {  
//        printf("%d ", rev[i]);  
//    }  
//}  
