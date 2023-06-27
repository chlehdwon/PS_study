#include <iostream>
#include <cstring>

using namespace std;
int cache[101][100001];
int info[101][2];
int n,k;

int dp(int item, int weight){
	if(item>n) return 0;
	int& ret = cache[item][weight];
	if(ret!=-1) return ret;
	ret = dp(item+1,weight);
	if(info[item][0]+weight<=k)
		ret = max(ret, dp(item+1,weight+info[item][0])+info[item][1]);
	return ret;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	memset(cache,-1,sizeof(cache));
	cin >> n >> k;
	for(int i=1; i<=n; ++i)
		cin >> info[i][0] >> info[i][1];
	cout << dp(1,0) << '\n';
	return 0;
}

/*
#include <iostream>
using namespace std;
int N;
int K;
int w[101];
int v[101];

int dp[100001];

int main() {
	cin>>N>>K;
	for(int i=0;i<N;i++)
		cin>>w[i]>>v[i];

		for(int i=0;i<N;i++)
		{
  			for(int j=K;j>=w[i];j--)
  			{
				if(dp[j]<dp[j-w[i]]+v[i])
				{
				  dp[j]=dp[j-w[i]]+v[i];
				}
  			}
		}
	cout<<dp[K]<<endl;

	return 0;
}
*/