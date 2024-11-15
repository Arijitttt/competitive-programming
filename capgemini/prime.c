//prime
#include<stdio.h>
#include<math.h>
int isPrime(int num){
	if(num<=1) return 0;
	int i;
	for(i=2;i<=sqrt(num);i++){
		if(num%i == 0){
			return 0;
		}
	}
	return 1;
}
int check_prime(int arr[],int n){
	int i,count = 0;
	for(i=0;i<n;i++){
		if(isPrime(arr[i])){
			count++;
		}
	}
	return count;
}
int main(){
	int arr[] = {2,3,4,5,6,7,8,9,11};
	int n = sizeof(arr)/sizeof(arr[0]);
	printf("number of prime numbers: %d",check_prime(arr,n));
	return 0;
}
