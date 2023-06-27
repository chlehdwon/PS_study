#include <iostream>
#include <cstring>

using namespace std;
int t,m,n,k,x,y,worm;
bool farm[50][50];

void check(int x, int y, int m, int n){
	farm[x][y]=0;
	if(x>0 && farm[x-1][y]==1) check(x-1,y,m,n);
	if(x<m-1 && farm[x+1][y]==1) check(x+1,y,m,n);
	if(y>0 && farm[x][y-1]==1) check(x,y-1,m,n);
	if(y<n-1 && farm[x][y+1]==1) check(x,y+1,m,n);
	
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> t;
	for(int i=0; i<t; ++i){
		cin >> m >> n >> k;
		for(int j=0; j<k; ++j){
			cin >> x >> y;
			farm[x][y] = 1;
		}
		for(int k=0; k<m; ++k){
			for(int l=0; l<n; ++l){
				if(farm[k][l]==1){
					worm+=1;
					check(k,l,m,n);
				}
			}
		}
		cout << worm << '\n';
		memset(farm, 0, sizeof(farm));
		worm=0;
	}
	
	
	return 0;
}