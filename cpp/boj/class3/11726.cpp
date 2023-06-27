#include <iostream>
#define MOD 10007

int n;
int dp[10000];

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	
	dp[0] = 1; dp[1] = 2;
	cin >> n;
	if(n>=2){
		for(int i=2; i<n; ++i){
			dp[i] = (dp[i-1] + dp[i-2]) % MOD;
		}
	}
	cout << dp[n-1] << '\n'; 
	
	return 0;
}