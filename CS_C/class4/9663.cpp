#include <iostream>
#include <vector>
#include <cstring>

bool column[15];
bool cross1[30];
bool cross2[30];
int n,cnt;

using namespace std;
void nqueen(int now){
	if(now==n){
		++cnt;
		return;
	}
	for(int i=0; i<n; ++i){
		if(!column[i]){
			int plus = i+now;
			int minus = now-i-1+n;
			if(!cross1[plus] && !cross2[minus]){
				column[i]=cross1[plus]=cross2[minus]=1;
				nqueen(now+1);
				column[i]=cross1[plus]=cross2[minus]=0;
			}
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	nqueen(0);
	cout << cnt << '\n';
	return 0;
}