#include <iostream>

using namespace std;
int virus=0;
bool connect[100][100];
bool status[100];

void recursive(int cpu, int n){
	for(int i=0; i<n; ++i){
		if(connect[cpu-1][i]==1 && status[i]==0){
			status[i]=1;
			++virus;
			recursive(i+1, n);
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	cin >> n >> m;
	for(int i=0; i<m; ++i){
		int a,b;
		cin >> a >> b;
		connect[a-1][b-1] = 1;
		connect[b-1][a-1] = 1;
	}
	status[0]=1;
	recursive(1, n);
	cout << virus << '\n';
	
	return 0;
}