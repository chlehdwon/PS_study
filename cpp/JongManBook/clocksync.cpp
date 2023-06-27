#include <iostream>
#include <cstring>
#define MAX 31
using namespace std;
int c,min_press;
int clocks[16];
bool switch_map[10][16]={
//   0 1 2 3 4 5 6 7 8 9101112131415
	{1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0},
	{0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1},
	{1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0},
	{0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0},
	{1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1},
	{0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1},
	{0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1},
	{0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},
	{0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0}
};

void click_switch(int idx){
	for(int i=0; i<16; ++i){
		if(switch_map[idx][i]==1){
			clocks[i]=(clocks[i]==3 ? 0 : clocks[i]+1);
		}
	}
	
	return;
}

bool issync(){
	for(int i=0; i<16; ++i)
		if(clocks[i]!=0) return false;
	return true;
}

void set_clock(int here, int cnt){
	if(issync()){
		if(cnt<min_press) min_press=cnt;
		return;
	}
	if(here==10) return;

	for(int i=0; i<4; ++i){
		set_clock(here+1,cnt+i);
		click_switch(here);
	}
	
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> c;
	while(c--){
		memset(clocks,0,sizeof(clocks));
		for(int i=0; i<16; ++i){
			int num;
			cin >> num;
			clocks[i] = (num%12)/3;
		}
		min_press=MAX;
		set_clock(0,0);
		if(min_press==MAX) cout << -1 << '\n';
		else cout << min_press << '\n';
	}
	return 0;
}