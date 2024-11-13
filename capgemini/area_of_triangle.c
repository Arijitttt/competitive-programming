//area of triangle
#include<stdio.h>
#include<math.h>
int main(){
	float a,b,s,c,area;
	printf("Enter 3 sides of triangle: ");
	scanf("%f%f%f",&a,&b,&c);
	s = (a+b+c)/2;
	area =s *(s-a)*(s-b)*(s-c);
	area = sqrt(area);
	printf("area of triangle is: %.2f",area);
	return 0;
}
