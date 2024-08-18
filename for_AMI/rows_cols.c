#include <stdio.h>
int main(){
	int arr[3][4] = {
		 {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
	};
	int rows = sizeof(arr)/sizeof(arr[0]);
	int col = sizeof(arr[0])/sizeof(arr[0][0]);
	printf("%d %d",rows,col);
	return 0;
}
