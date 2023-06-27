#include <iostream>
#include <cstring>

using namespace std;
int c,n;
int board[5][5];
int search[8][2] = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
int cache[5][5][10];
bool pass;
string word;

void recursive(int x, int y, int index, string& word){
	cache[x][y][index]=1;
	if(index==word.size()-1){
		pass=1;
		return;
	}
	char target=word[index+1];
	for(int i=0; i<8; ++i){
		int new_x = x+search[i][0];
		int new_y = y+search[i][1];
		if(new_x<0 || new_x>=5 || new_y<0 || new_y>=5) continue;
		if(board[new_x][new_y]==target){
			if(cache[new_x][new_y][index+1]==1) continue;
			recursive(new_x, new_y, index+1, word);
		}
	}
	return;
}
	
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> c;
	while(c--){
		for(int i=0; i<5; ++i){
			string row;
			cin >> row;
			for(int j=0; j<5; ++j){
				board[i][j]=row[j];
			}
		}
		cin >> n;
		while(n--){
			pass=0;
			cin >> word;
			int size = word.size();
			memset(cache,0,sizeof(cache));
			for(int i=0; i<5; ++i){
				for(int j=0; j<5; ++j){
					if(board[i][j]==word[0]){
						recursive(i,j,0,word);
					}
					if(pass)
						break;
				}
				if(pass)
					break;
			}
			if(!pass)
				cout << word << " NO" << '\n';
			else
				cout << word << " YES" << '\n';
		}
	}
	return 0;
}