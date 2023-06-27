#include <iostream>
#include <tuple>
#include <queue> 
#include <cstring>
#define INF 987654321
#define MAX 1001
using namespace std;
int map[MAX][MAX];
int choice[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
bool visited[MAX][MAX][2];
int n,m;

void bfs(){
	int min_dist = INF;
	queue<tuple<int,int,int,bool>> q;
	visited[1][1][1]=1;
	q.push(make_tuple(1,1,1,1));
	while(!q.empty()){
		auto now  = q.front();
		q.pop();
		int y = get<0>(now);
		int x = get<1>(now);
		int dist = get<2>(now);
		bool wall = get<3>(now);
		if(y==n && x==m){
			min_dist = dist;
			break;
		}
		for(int i=0; i<4; ++i){
			int ny = y+choice[i][0];
			int nx = x+choice[i][1];
			if(ny<=0 || ny>n || nx<=0 || nx>m) continue;
			if(map[ny][nx]==0 && !visited[ny][nx][wall]){
				visited[ny][nx][wall]=1;
				q.push(make_tuple(ny,nx,dist+1,wall));
			}
			if(map[ny][nx]==1 && wall && !visited[ny][nx][!wall]){
				visited[ny][nx][!wall]=1;
				q.push(make_tuple(ny,nx,dist+1,!wall));
			}
		}
	}
	
	if(min_dist==INF) cout << -1 << '\n';
	else cout << min_dist << '\n';
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n >> m;
	for(int i=1; i<=n; ++i){
		string nums;
		cin >> nums;
		for(int j=1; j<=m; ++j)
			map[i][j]=nums[j-1]-'0';
	}
	bfs();
	
	return 0;
}