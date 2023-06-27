#include <iostream>
#include <cstring>

using namespace std;
int cache[501][501];
int value[501][501];
int n;

int dp(int y, int x){
	if(y==n) return value[y][x];
	int& ret = cache[y][x];
	if(ret!=-1) return ret;
	return (ret = value[y][x]+max(dp(y+1,x),dp(y+1,x+1)));
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	memset(cache,-1,sizeof(cache));
	for(int y=1; y<=n; ++y){
		for(int x=1; x<=y; ++x){
			cin >> value[y][x];
		}
	}
	cout << dp(1,1) << '\n';
	return 0;
}