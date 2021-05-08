#include <iostream>
#include <cstring>
using namespace std;
int c,h,w,total;
int board[20][20];
int direct[4][2][2]={
	{{0,1},{1,0}},
	{{0,1},{1,1}},
	{{1,0},{1,1}},
	{{1,0},{1,-1}}
};

void board_cover(){
	int white_counter = 0;
	for(int i=0; i<h; ++i){
		for(int j=0; j<w; ++j){
			if(board[i][j]==0) white_counter++;
		}
	}
	if(white_counter==0){
		total+=1;
		return;
	}
	for(int i=0; i<h; ++i){
		for(int j=0; j<w; ++j){
			if(board[i][j]==0){
				for(int k=0; k<4; ++k){
					int i_1 = i+direct[k][0][0];
					int j_1 = j+direct[k][0][1];
					int i_2 = i+direct[k][1][0];
					int j_2 = j+direct[k][1][1];
					if(i_1>=h || j_1 >=w || i_2>=h || j_2>=w || j_2<0) continue;
					if(board[i_1][j_1]==0 && board[i_2][j_2]==0){
						board[i][j] = board[i_1][j_1] = board[i_2][j_2] = 1;
						board_cover();
						board[i][j] = board[i_1][j_1] = board[i_2][j_2] = 0;
					}
				}
				return;
			}
		}
	}
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> c;
	while(c--){
		total=0;
		int white_counter=0;
		memset(board,0,sizeof(board));
		cin >> h >> w;
		for(int i=0; i<h; ++i){
			string inputs;
			cin >> inputs;
			for(int j=0; j<w; ++j){
				board[i][j] = (inputs[j]=='#' ? 1 : 0);
				if(board[i][j]==0) white_counter++;
			}
		}
		if(white_counter%3){
			cout << 0 << '\n';
			continue;
		}
		if(white_counter==0){
			cout << 1 << '\n';
			continue;
		}
		board_cover();
		cout << total << '\n';
	}
	
	return 0;
}