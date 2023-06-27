#include <cstdio>
#include <algorithm>

int change_counter(int y, int x, char map[50][50]);
int main(){
	int row,col,cnt,min_cnt=32;
	char map[50][50];
	scanf("%d %d\n", &row, &col);
	for(int i=0; i<row; i++){
		scanf("%s", &map[i]);
	}
	for(int y=0; y<row-7; y++){
		for(int x=0; x<col-7; x++){
			cnt = change_counter(y, x, map);
			if(min_cnt > cnt) min_cnt=cnt;
		}
	}
	
	printf("%d\n", min_cnt);

	return 0;
}

int change_counter(int y, int x, char map[50][50]){
	int cnt=0;
	char bw[2] = {'B', 'W'};
	for(int i=0; i<8; i++){
		for(int j=0; j<8; j++){
			if(bw[(i+j)%2] == map[y+i][x+j]) cnt++; 
		}
	}
	cnt = cnt<32 ? cnt : 64-cnt;
	
	return cnt;
}