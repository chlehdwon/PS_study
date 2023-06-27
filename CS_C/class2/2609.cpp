#include <iostream>

using namespace std;
int gcd(int a, int b){
	if(b==0) return a;
	else return gcd(b, a%b);
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0);

	int a, b;
	cin >> a >> b;
	cout << gcd(a,b) << "\n" << a*b/gcd(a,b) << endl;
}

