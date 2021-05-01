#include <iostream>
using namespace std;
int recursion(int n){
	if(n==1) return 0;
	if(n==2 || n==3) return 1;
	return min(n%3+1+recursion(n/3), n%2+1+recursion(n/2));
}
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int num;
	cin >> num;
	cout << recursion(num) << '\n';
	return 0;
}