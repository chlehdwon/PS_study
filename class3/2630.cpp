#include <iostream>


int n, white=0, blue=0;
bool paper[128][128];

using namespace std;
bool is_all_same(int x, int y, int width){
	bool target = paper[x][y];
	for(int i=x; i<x+width; ++i){
		for(int j=y; j<y+width; ++j){
			if(target^paper[i][j])
				return 0;
		}
	}
	if(target) blue+=1;
	else white+=1;
	return 1;
}

void recursion(int x, int y, int width){
	if(width==1){
		if(paper[x][y]==0) white+=1;
		else blue+=1;
		return;
	}
	
	int half = width/2;
	if(!is_all_same(x,y,width)){
		if(!is_all_same(x,y,half)){
			recursion(x,y,half);
		}
		if(!is_all_same(x+half,y,half)){
			recursion(x+half,y,half);
		}
		if(!is_all_same(x,y+half,half)){
			recursion(x,y+half,half);
		}
		if(!is_all_same(x+half,y+half,half)){
			recursion(x+half,y+half,half);
		}
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin>>n;
	for(int i=0; i<n; ++i){
		for(int j=0; j<n; ++j){
			cin>>paper[i][j];
		}
	}
	recursion(0,0,n);

	cout << white << "\n" << blue << "\n";
	
	return 0;
}