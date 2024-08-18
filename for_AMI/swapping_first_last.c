#include <stdio.h>
int swapping_first_last(int arr[][4],int rows,int cols){
	int i,c;
	int x = 0;
	int y = rows-1; 
	for(i=0;i<cols;i++){
		c = arr[x][i];
		arr[x][i]=arr[y][i];
		arr[y][i]=c;
	}
	return 0;
}
int main(){
	int arr[3][4] = {
		 {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int rows = sizeof(arr)/sizeof(arr[0]);
    int cols = sizeof(arr[0])/sizeof(arr[0][0]);
    swapping_first_last(arr,rows,cols);
    int i,j;
    for(i=0;i<rows;i++){
    	for(j=0;j<cols;j++){
    		printf("%d ",arr[i][j]);
		}
    	printf("\n");
	}
}
