//occur_times
#include<stdio.h>
int main(){
	int nums[] = {1,2,3,3,4,1,4,5,1,2};
	int freq[101] = {0};
	int n = sizeof(nums)/sizeof(nums[0]);
	int i,j=0;
	for(i=0;i<n;i++){
		freq[nums[i]]++;
	}
	for(i=0;i<n;i++){
		if(freq[i]>0){
			printf("%d ocuurs %d times\n",i,freq[i]);
		}
	}
	return 0;
}
