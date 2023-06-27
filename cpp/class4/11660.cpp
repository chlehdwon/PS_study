#include <iostream>
#include <vector>

using namespace std;
int arr[1025][1025];
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	cin >> n >> m;
	for(int i=1; i<=n; ++i){
		for(int j=1; j<=n; ++j){
			int num;
			cin >> num;
			arr[i][j]=arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]+num;
		}
	}
	for(int i=0; i<m; ++i){
		int x1,y1,x2,y2;
		cin >> y1 >> x1 >> y2 >> x2;
		cout << arr[y2][x2] - arr[y1-1][x2] - arr[y2][x1-1] + arr[y1-1][x1-1] << '\n';
	}
	
	return 0;
}