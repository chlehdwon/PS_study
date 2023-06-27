#include <iostream>
#include <vector>
#include <queue>
#define MAX 500
#define INF 987654321

using namespace std;

vector<pair<int,int>> vec[MAX+1];
int d[MAX+1];

bool wormhole(int start, int n){
	bool cycle = false;
	queue<pair<int,int>> pq;
	d[start]=0;
	pq.push(make_pair(0,start));
	for(int i=1; i<=n; ++i){
		for(int j=1; j<=n; ++j){
			for(auto p : vec[j]){
				if(d[p.first]>p.second+d[j]){
					d[p.first] = p.second + d[j];
					if(i==n) cycle = true;
				}
			}
		}
	}
	
	return cycle;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int tc;
	cin >> tc;
	while(tc--){
		int n,m,w,s,e,t;
		for(int i=1; i<=MAX; ++i){
			vec[i].clear();
			vec[i].clear();
		}
		for(int i=1; i<=MAX; ++i)
			d[i]=INF;
		cin >> n >> m >> w;
		for(int i=0; i<m; ++i){
			cin >> s >> e >> t;
			vec[s].push_back(make_pair(e,t));
			vec[e].push_back(make_pair(s,t));
		}
		for(int i=0; i<w; ++i){
			cin >> s >> e >> t;
			vec[s].push_back(make_pair(e,-t));
		}
		if(wormhole(1, n)) cout << "YES\n";
		else cout << "NO\n";
	}
	
	return 0;
}