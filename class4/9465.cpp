#include <iostream>
#include <cstring>

using namespace std;
int cache[100001][3];
int price[2][100001];
int n,m;

int dp(int x, int flag){
	// flag -> 0:we can pick both, 1:only top, 2: only bottom
	if(x==m){
		if(flag==0) return max(price[0][m],price[1][m]);
		else if(flag==1) return price[0][x];
		else return price[1][x];
	}
	
	int& ret = cache[x][flag];
	if(ret!=-1) return ret;
	ret = dp(x+1,0);
	if(flag!=2) ret = max(ret, price[0][x]+dp(x+1,2));
	if(flag!=1) ret = max(ret, price[1][x]+dp(x+1,1));
	return ret;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	while(n--){
		memset(cache,-1,sizeof(cache));
		memset(price,0,sizeof(price));
		cin >> m;
		for(int i=1; i<=m; ++i){
			cin >> price[0][i];
		}
		for(int i=1; i<=m; ++i){
			cin >> price[1][i];
		}
		cout << dp(1,0) << '\n';
	}
	
	return 0;
}