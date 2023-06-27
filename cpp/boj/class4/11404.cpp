#include <iostream>
#include <vector>
#define INF 987654321
#define MAX 100

using namespace std;
int dist[MAX+1][MAX+1];

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m,a,b,c;
	for(int i=1; i<MAX+1; ++i)
		for(int j=1; j<MAX+1; ++j)
			if(i!=j) dist[i][j]=INF;
	cin >> n >> m;
	for(int i=0; i<m; ++i){
		cin >> a >> b >> c;
		dist[a][b] = min(dist[a][b],c);
	}
	for(int i=1; i<=n; ++i){
		for(int j=1; j<=n; ++j){
			for(int k=1; k<=n; ++k){
				if(dist[j][k]>dist[j][i]+dist[i][k])
					dist[j][k]=dist[j][i]+dist[i][k];
			}
		}
	}
	for(int i=1; i<=n; ++i){
		for(int j=1; j<=n; ++j){
			if(dist[i][j]==INF) cout << 0 << " ";
			else cout << dist[i][j] << " ";
		}
		cout << '\n';
	}
		
	return 0;
}