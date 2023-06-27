#include <iostream>
#include <vector>

using namespace std;
vector<pair<int,int>> tree[100001];
int diameter = 0;

int depth(int n, int parent){
	if(tree[n].size()<2) return 0;
	int first=0, second=0;
	for(int i=0; i<tree[n].size(); ++i){
		int node = tree[n][i].first;
		int dist = tree[n][i].second;
		if(node==parent) continue;
		int radius = depth(node,n)+dist;
		if(radius>first){
			int temp = first;
			first = radius;
			second = temp;
		}
		else if(radius>second)
			second = radius;
	}
	if(diameter<first+second) diameter = first+second;
	
	return first;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	for(int i=1; i<=n; ++i){
		int node, dist, parent;
		cin >> parent;
		while(true){
			cin >> node;
			if(node==-1) break;
			cin >> dist;
			tree[parent].push_back(make_pair(node, dist));
		}
	}
	tree[1].push_back(make_pair(0,0));
	depth(1,0);
	cout << diameter << '\n';
	return 0;
}