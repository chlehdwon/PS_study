// 2300-2323
#include <iostream>
#include <queue>

using namespace std;

typedef struct Data {
    int x, y, day;
}Data;

int n,m,count_0,days;
int tomato[1000][1000];
queue<Data> q;

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n >> m;
	for(int i=0; i<m; ++i){
		for(int j=0; j<n; ++j){
			cin >> tomato[i][j];
			if(tomato[i][j]==1) q.push((Data){i,j,0});
			if(tomato[i][j]==0) count_0+=1;
		}
	}
	while(!q.empty()){
		Data d = q.front();
		int i = d.x;
		int j = d.y;
		days=d.day;
		if(i>0 && tomato[i-1][j]==0){
			count_0-=1;
			tomato[i-1][j]=1;
			q.push((Data){i-1,j,days+1});
		}
		if(i<m-1 && tomato[i+1][j]==0){
			count_0-=1;
			tomato[i+1][j]=1;
			q.push((Data){i+1,j,days+1});
		}
		if(j>0 && tomato[i][j-1]==0){
			count_0-=1;
			tomato[i][j-1]=1;
			q.push((Data){i,j-1,days+1});	
		}
		if(j<n-1 && tomato[i][j+1]==0){
			count_0-=1;
			tomato[i][j+1]=1;
			q.push((Data){i,j+1,days+1});
		}
		q.pop();
	}
	
	if(count_0) cout << -1 <<'\n';
	else cout << days << '\n';
	
	return 0;
}