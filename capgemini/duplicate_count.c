// duplicate
#include<stdio.h>
int main(){
	int nums[] = {1, 2, 1, 3, 7, 9, 4, 1, 5, 8, 9, 1, 5, 4, 1, 3, 4, 5, 6, 7, 8, 9, 10};
	int n = sizeof(nums)/sizeof(nums[0]);
	int freq[101] = {0};
	int i,count = 0;
	int x[101];
	for (i=0;i<n;i++){
		freq[nums[i]]++;
	}
	for(i=0;i<n;i++){
		if(freq[i]>0){
			x[count] = i;
			count++;
			printf("%d : %d\n",i,freq[i]);
		}
	}
	printf("unique elements:\n");
	for(i=0;i<count;i++){
		printf("%d ",x[i]);
	}
	return 0;
}
