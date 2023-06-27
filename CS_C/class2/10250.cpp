#include <iostream>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int t, h, w, n, x, y;
	cin>>t;
	for(int i=0; i<t; ++i){
		cin>>h>>w>>n;
		x=n%h>0 ? n%h : h;
		y=n%h>0 ? n/h+1 : n/h;
		if(y<10) cout<<x<<0<<y<<'\n';
		else cout<<x<<y<<'\n';
	}
	
	return 0;
}