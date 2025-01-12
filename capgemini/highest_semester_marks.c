//semester marks
#include <stdio.h>
int main(){
	int n;
	printf("\nEnter number of semester: ");
	scanf("%d",&n);
	int i,j,k,max_mark = -1,subjects;
	for(i=1;i<=n;i++){
		printf("Enter number of subject in %dsemester: ",i);
		scanf("%d",&subjects);
		printf("\nmarks obtained in semster %d",i);
		for(j=1;j<=subjects;j++){
			int mark;
			scanf("%d",&mark);
			if(mark < 0 || mark > 100){
				printf("\n you have entered invalid marks");
				return 1;
			}
			if(mark > max_mark){
				max_mark = mark;
			}
		}
		printf("\nmaximum marks in semester %d : %d",i,max_mark);
	}
	return 0;
}
