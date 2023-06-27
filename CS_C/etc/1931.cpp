//2319-2348
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,last=0,num=0;
	cin >> n;
	vector<pair<int,int>> schedule(n);
	for(int i=0; i<n; ++i){
		cin >> schedule[i].second;
		cin >> schedule[i].first;
	}
	sort(schedule.begin(),schedule.end());
	for(auto pair:schedule){
		if(last<=pair.second){
			num+=1;
			last=pair.first;
		}
	}	
	cout << num << '\n';

	return 0;
}