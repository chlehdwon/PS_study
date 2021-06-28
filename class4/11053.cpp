#include <iostream>
#include <cstring>

using namespace std;
int n;
int arr[1001]={-1,};;
int cache[1001];

int dp(int m){
	int &ret = cache[m];
	if(ret!=-1) return ret;
	ret=0;
	for(int i=m+1; i<=n; ++i){
		if(arr[i]>arr[m]) ret=max(ret,1+dp(i));
	}
	
	return ret;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	memset(cache,-1,sizeof(cache));
	for(int i=1; i<=n; ++i){
		cin >> arr[i];
	}
	cout << dp(0) << '\n';
	
	return 0;
}