#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
string cache[101][101];
int n,m;

string add(string a, string b){
	string ret;
	int sum=0;
	while(!a.empty() || !b.empty() || sum){
		if(!a.empty()){
			sum+=a.back()-'0';
			a.pop_back();
		}
		if(!b.empty()){
			sum+=b.back()-'0';
			b.pop_back();
		}
		ret.push_back((sum%10)+'0');
		sum/=10;
	}
	reverse(ret.begin(),ret.end());
	return ret;
}

string comb(int n, int m){
	if(n==m || m==0) return "1";
	string& ret = cache[n][m];
	if(!ret.empty()) return ret;
	else return (ret = add(comb(n-1,m-1),comb(n-1,m)));
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n >> m;
	cout << comb(n,m) << '\n';
	
	return 0;
}