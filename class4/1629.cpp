#include <iostream>

using namespace std;

long long multiply(int a, int b, int c){
	if(b==0) return 1;
	if(b==1) return (long long)a%c;
	if(b==2) return (long long)a*a%c;
	int half = b/2;
	if(b%2==1) return multiply(multiply(a,half,c),2,c)*a%c;
	else return multiply(multiply(a,half,c),2,c);
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int a,b,c;
	cin >> a >> b >> c;
	cout << multiply(a,b,c) << '\n';
	
	return 0;
}