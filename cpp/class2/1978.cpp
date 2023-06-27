#include <cstdio>
#include <cmath>

int is_prime(int num){
	if(num<=1) return 0;

	for(int i=2; i*i<=num; i++){
		if(num%i==0) return 0;
	}
	return 1;
}


int main(){
	int n, num, nums_of_prime=0;
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d", &num);
		nums_of_prime+=is_prime(num);
	}
	
	printf("%d\n", nums_of_prime);
	
	return 0;
}