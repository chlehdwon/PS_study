#include <iostream>
#include <unordered_set>
#include <vector>
#include <utility>

using namespace std;
int n, m, x, y, num=0;
bool graph[1000][1000];

void check(int num, int n){
	// it means we already visit check(num, n) so skip
	if(!graph[num][num]) return;
	graph[num][num]=0;
	for(int i=0; i<n; ++i){
		// if there is any connected element, check that element.
		if(graph[num][i]){
			graph[num][i]=0;
			graph[i][num]=0;
			check(i, n);
		}
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n >> m;
	for(int i=0; i<n; ++i){
		graph[i][i]=1;
	}
	for(int i=0; i<m; ++i){
		cin >> x >> y;
		graph[x-1][y-1]=1;
		graph[y-1][x-1]=1;
	}

	for(int i=0; i<n; ++i){
		// if we have not call check(i, n), increase num and check it.
		if(graph[i][i]){
			++num;
			check(i, n);
		}
		
	}
	
	cout << num << '\n';
	
	return 0;
}