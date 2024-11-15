#include <stdio.h>

int main() {
    char nums[] = "aabbbbeeeeffggg";
    
    int freq[256] = {0};
    
    int n = sizeof(nums)-1;
    int i;
    for(i=0;i<n;i++){
    	freq[nums[i]]++;
	}
	for(i=0;i<256;i++){
		if(freq[i]>0){
			printf("%c%d",i,freq[i]);
		}
	}

    return 0;
}

