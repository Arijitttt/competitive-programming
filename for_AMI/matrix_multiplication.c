#include <stdio.h>

int main() {
	int m[3][3];
    int a[3][3] = {
        {5, 4, 3},
        {9, 2, 1},
        {8, 6, 7}
    };
    
    int b[3][3] = {
        {9, 1, 7},
        {6, 4, 8},
        {2, 5, 3}
    };
    
    int i, j,k,s;
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			s = 0;
			for(k=0;k<3;k++){
				s = s+ a[i][k] * b[k][j];
			}
			m[i][j] = s;
		}
	}
	
	printf("matrix multip;lication\n");
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			printf("%d ",a[i][j]);
		}
		printf("\t");
		for(j=0;j<3;j++){
			printf("%d ",b[i][j]);
		}
		printf("\t");
		for(j=0;j<3;j++){
			printf("%d ",m[i][j]);
		}
		printf("\n");
	}
    
    return 0;
}

