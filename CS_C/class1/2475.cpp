#include <cstdio>

int main(){
	int n1,n2,n3,n4,n5,verify;
	scanf("%d %d %d %d %d", &n1, &n2, &n3, &n4, &n5);
	verify=(n1*n1+n2*n2+n3*n3+n4*n4+n5*n5)%10;
	printf("%d\n", verify);
	
	return 0;
}