int krishnamurti_number(int n){
	int s=0,i,t;
	while(n>0){
		int fact = 1;
		t = n%10;
		for(i=1;i<=t;i++){
			fact = fact*i;
		}
		s = s+fact;
		n = n/10;
	}
	return s;
}
int main(){
	int p,n = 145;
	p =krishnamurti_number(n);
	if(p == n){
		printf("%d krishnamurti number",p);
	}
	else{
		printf("not");
	}
}
