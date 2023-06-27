#include <iostream>
#include <vector>

using namespace std;
void print(vector<int>& a){
	for(auto& ele : a) {
        cout << ele << ' ';
    }
	cout << '\n';
	
	return;
}

void recursive(vector<int>& a, int n, int m){
	int len = a.size();
	if(len==m){
		print(a);
		return;
	}
	int last = 0;
	if(!a.empty()) last = a[len-1];
	for(int i=last+1; i<n-len+m; ++i){
		a.push_back(i);
		recursive(a,n,m);
		a.pop_back();
	}
	
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	cin >> n >> m;
	vector<int> a={};
	recursive(a,n,m);
	
	return 0;
}