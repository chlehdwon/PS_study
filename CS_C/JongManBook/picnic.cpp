#include <iostream>
#include <cstring>

using namespace std;
int c,n,m,total;
bool graph[10][10];
int is_friend[10];

void pairing(int n){
	int target=-1;
	for(int i=0; i<n; ++i){
		if(is_friend[i]==0){
			target=i;
			break;
		}
	}
	if(target==-1){
		total+=1;
		return;
	}
	for(int i=0; i<n; ++i){
		if(graph[target][i]==1 && is_friend[i]==0){
			is_friend[i]=1; is_friend[target]=1;
			pairing(n);
			is_friend[i]=0; is_friend[target]=0;
		}
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> c;
	for(int i=0; i<c; ++i){
		memset(graph,0,sizeof(graph));
		memset(is_friend,0,sizeof(is_friend));
		total=0;
		cin >> n >> m;
		for(int j=0; j<m; ++j){
			int a,b;
			cin >> a >> b;
			graph[a][b]=1;
			graph[b][a]=1;
		}
		pairing(n);
		cout << total << '\n';
	}
	
	return 0;
}