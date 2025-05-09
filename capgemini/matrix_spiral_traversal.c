#include<stdio.h>
void spiralTraversal(int rows,int cols, int matrix[rows][cols]){
	int top = 0, bottom = rows-1;
	int left = 0, right = cols -1;
	while(top<=bottom && left <= right){
		int i;
		for(i=left;i<=right;i++){
			printf("%d ",matrix[top][i]);
		}
		top++;
		for(i=top;i<=bottom;i++){
			printf("%d ",matrix[i][right]);
		}
		right--;
		if(top<=bottom){
			for(i = right;i>=left;i--){
				printf("%d ",matrix[bottom][i]);
			}
			bottom--;
		}
		if(left<=right){
			for(i=bottom;i>=top;i--){
				printf("%d ",matrix[i][left]);
			}
			left++;
		}
	}
}
int main(){
	int rows,cols;
	printf("Enter number of erows and colums: ");
	scanf("%d%d",&rows,&cols);
	int matrix[rows][cols];
	printf("\nEnyer matrix element:\n");
	int i,j;
	for(i=0;i<rows;i++){
		for(j=0;j<cols;j++){
			scanf("%d",&matrix[i][j]);
		}
	}
	printf("\nSpiral traversal of the matrix\n");
	spiralTraversal(rows,cols,matrix);
}
