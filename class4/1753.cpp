#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#define MAX 987654321

using namespace std;
vector<pair<int,int>> map[20001];
int d[20001];
int v,e,k;

void solve(int start){
	auto cmp = [](pair<int,int> left, pair<int,int> right) {return left.second > right.second;};
	priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(cmp)> pq(cmp);
	d[start]=0;
	pq.push(pair<int,int>(start,0));
	while(!pq.empty()){
		int current = pq.top().first;
		int cost = pq.top().second;
		pq.pop();
		if(d[current] < cost) continue;
		for(int i=0; i<map[current].size(); ++i){
			int next = map[current][i].first;
			int next_cost = map[current][i].second;
			if(d[next] > cost + next_cost){
				d[next] = cost + next_cost;
				pq.push(pair<int,int>(next,d[next]));
			}
		}
	}
	
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> v >> e >> k;
	for(int i=0; i<e; ++i){
		int a,b,cost;
		cin >> a >> b >> cost; 
		map[a].push_back(pair<int,int>(b,cost));
	}
	for(int i=1; i<=v; ++i) d[i]= MAX;
	solve(k);
	for(int i=1; i<=v; ++i){
		if(d[i]==MAX) cout << "INF" << '\n';
		else cout << d[i] << '\n';
	}
	
	return 0;
}