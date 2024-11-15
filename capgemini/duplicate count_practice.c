//duplicate count_practice
#include<stdio.h>
int main(){
	int nums[] = {1, 2, 1, 3, 7, 9, 4, 1, 5, 8, 9, 1, 5, 4};
	int freq[101] = {0};
	int x[101];
	int n = sizeof(nums)/sizeof(nums[0]);
	int i,j=0;
	for(i=0;i<n;i++){
		freq[nums[i]]++;
	}
	for(i=0;i<101;i++){
		if(freq[i]>0){
			printf("%d appears %d time",i,freq[i]);
			x[j] = i;
			j++;
		}
	}
	for(i=0;i<j;i++){
		printf("%d ",x[i]);
	}
	return 0;
}
