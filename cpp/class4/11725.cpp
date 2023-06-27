#include <iostream>
#include <vector>

using namespace std;
int n;
int parent[100001];
vector<vector<int>> map{100001};

void find(int node){
	for(int i=0; i<map[node].size(); ++i){
		int target = map[node][i];
		if(target>1 && parent[target]==0){
			parent[target]=node;
			find(target);
		}
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	for(int i=0; i<n-1; ++i){
		int a,b;
		cin >> a >> b;
		map[a].push_back(b);
		map[b].push_back(a);
	}
	find(1);
	for(int i=2; i<=n; ++i){
		cout << parent[i] << '\n';
	}
	
	return 0;
}