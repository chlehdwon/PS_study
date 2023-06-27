#include <iostream>
#include <cstring>
#define MAX 987654321

using namespace std;
int cache[1001][3];
int cost[1001][3];
int n;

int dp(int num, int flag){
	if(num==n) return cost[n][flag];
	int& ret = cache[num][flag];
	if(ret!=-1) return ret;
	int now = cost[num][flag];
	ret = MAX;
	for(int i=0; i<3; ++i){
		if(flag!=i){
			ret = min(ret, dp(num+1,i)+now);
		}
	}
	
	return ret;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	memset(cache,-1,sizeof(cache));
	for(int i=1; i<=n; ++i){
		cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
	}
	int max_cost = MAX;
	for(int i=0; i<3; ++i){
		max_cost = min(max_cost, dp(1,i));
	}
	cout << max_cost << '\n';
	
	return 0;
}