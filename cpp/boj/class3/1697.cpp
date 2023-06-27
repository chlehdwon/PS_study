#include <iostream>
#include <algorithm>

using namespace std;
int recursive(int x, int y){
	int temp=y;
	if(x>=y) return x-y;
	if(y==x*2 || y==x+1) return 1;
	if(x*2>y)
		temp = min(x*2-y+1, y-x);
	if(y%2==0) return min(temp, recursive(x,y/2)+1);
	else return min(min(recursive(x,(y+1)/2), recursive(x,(y-1)/2))+2, temp);
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int x,y;
	cin >> x >> y;
	cout << recursive(x, y) << '\n';
	return 0;
}