#include <iostream>
#include <vector>

using namespace std;
vector<pair<int,int>> tree[10000];
int max_diameter = 0;

int depth(int n){
	if(tree[n].size()==0) return 0;
	int first=0, second=0;
	for(int i=0; i<tree[n].size(); ++i){
		int radius = depth(tree[n][i].first)+tree[n][i].second;
		if(radius>first){
			int temp = first;
			first = radius;
			second = temp;
		}
		else if(radius>second)
			second = radius;
	}
	if(max_diameter<first+second) max_diameter=first+second;
	return first;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	for(int i=1; i<n; ++i){
		int parent, child, cost;
		cin >> parent >> child >> cost;
		tree[parent].push_back(make_pair(child,cost));
	}
	
	depth(1);
	
	cout << max_diameter << '\n';
	return 0;
}