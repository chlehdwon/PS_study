#include <iostream>
#include <cstring>

using namespace std;
int c,min_press;
int clocks[16];
int press[10];
bool switch_map[10][16]={
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
void set_clock(int times, int start){
	for(int i=0; i<10; ++i){
		cout << press[i] << ' ';
	}
	cout << '\n';
	if(times>=min_press) return;
	int twelve_now=0;
	for(int i=0; i<16; ++i){
		if(clocks[i]==0) twelve_now++;
	}
	if(twelve_now==16){
		if(times<min_press) min_press=times;
		return;
	}
	
	for(int i=start; i<10; ++i){
		if(press[i]<3){
			press[i]+=1;
			for(int j=0; j<16; ++j){
				if(switch_map[i][j]==1){
					clocks[j] = (clocks[j]==3 ? 0 : clocks[j]+1);
				}
			}
			set_clock(times+1, i+1);
		}
	}
	
	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> c;
	while(c--){
		memset(clocks,0,sizeof(clocks));
		memset(press,0,sizeof(press));
		for(int i=0; i<16; ++i){
			int num;
			cin >> num;
			clocks[i] = (num%12)/3;
		}
		min_press=31;
		int times=0;
		set_clock(times,0);
		if(min_press==31) cout << -1 << '\n';
		else cout << min_press << '\n';
	}
	return 0;
}