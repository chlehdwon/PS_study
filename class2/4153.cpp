#include <iostream>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0);
	int a,b,c;
	while(1){
		cin>>a>>b>>c;
		if(!a || !b || !c) break;
		int maximum = max(max(a,b),c);
		if(a*a+b*b+c*c == maximum*maximum*2) cout << "right" << endl;
		else cout << "wrong" << endl;
	}
	
	return 0;
}