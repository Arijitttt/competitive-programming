int symetric_matrix(int arr[],int rows,int cols){
	int i,j;
	for(i=0;i<rows;i++){
		for(j=0;j<cols;j++){
			if(m[i][j]==m[j][i]){
				return 1;
			}
		
		}
	}
	return -1;
}
int main(){
	int arr[3][3]={
	{5,2,1},
	{2,8,2},
	{1,2,5}

	}
}
