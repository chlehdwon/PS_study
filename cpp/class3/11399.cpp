#include <iostream>
#include <map>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n, time, sum=0;
	multimap<int, int> atm;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> time;
		atm.insert({time, i+1});
	}
	for(auto itr = atm.begin(); n>0; --n, ++itr){
		sum+=n*(itr->first);
	}
	cout << sum << "\n";
	
	
	return 0;
}