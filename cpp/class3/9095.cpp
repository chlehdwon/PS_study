#include <cstdio>

int main(){
	int dp[11] = {1, 2, 4};
	int len[1000];
	// the number of testcases
	int n;
	// the max value which we have to calculate
	int max = 3;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &len[i]);
		// find max value of the inputs
		if(max < len[i]) max = len[i];
	}

	for(int i=3; i<max; i++){
		// calculate the number of cases by using dp
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]; 
	}
	
	for(int i=0; i<n; i++){
		// print each calculated nubmer
		printf("%d\n", dp[len[i]-1]);
	}
	
	return 0;
}