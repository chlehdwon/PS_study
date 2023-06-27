#include <iostream>

using namespace std;
int recursive(int n, int r, int c){
	if(n==1) return 2*r+c;
	int half = 1<<(n-1);
	switch((r/half)*2+c/half){
		case 0:
			return recursive(n-1, r, c);
			break;
		case 1:
			return half*half+recursive(n-1, r, c-half);
			break;
		case 2:
			return half*half*2+recursive(n-1, r-half, c);
			break;
		case 3:
			return half*half*3+recursive(n-1, r-half, c-half);
			break;
		default:
			break;
	}
	return -1;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,r,c;
	cin >> n >> r >> c;
	cout << recursive(n,r,c) << '\n';
	
	
	return 0;
}