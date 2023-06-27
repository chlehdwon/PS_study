#include <cstdio>

int main(){
	int n, sum=0;
	char *nums;
	scanf("%d", &n);
	scanf("%s", nums);
	while(n--){
		sum+=nums[n-1]-'0';
	}
	
	printf("%d\n", sum);
	
	return 0;
}