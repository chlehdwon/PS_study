#include <iostream>
#include <vector>
#define MOD 1000000007ll
using namespace std;
vector<long long> fibo(long long n){
	if(n==0) return {1,0};
	if(n==1) return {1,1};
	if(n==2) return {2,1};
	vector<long long> half = fibo(n/2);
	vector<long long> ans{2};
	long long a = half[0]*half[0]+half[1]*half[1];
	long long b = (half[0]*half[1]*2%MOD-half[1]*half[1]%MOD+MOD)%MOD;
	if(n%2==0){
		ans[0]=a%MOD;
		ans[1]=b%MOD;
		return ans;
	}
	else{
		ans[0]=(a+b)%MOD;
		ans[1]=a%MOD;
		return ans;
	}
	
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	long long n;
	cin >> n;
	vector<long long> ans = fibo(n);
	cout << ans[1] << '\n';
	cout << '\n';
	return 0;
}