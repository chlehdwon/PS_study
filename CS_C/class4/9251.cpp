#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int cache[1001][1001];
string a,b;

int solve(int m, int n){
	if(m>a.size() || n>b.size()) return 0;
	int& ret = cache[m][n];
	if(ret!=-1) return ret;
	if(a[m-1]==b[n-1]) return (ret=1+solve(m+1,n+1));
	else return (ret=max(solve(m+1,n),solve(m,n+1)));
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	memset(cache,-1,sizeof(cache));
	cin >> a >> b;
	cout << solve(1,1) << '\n';
	
	return 0;
}