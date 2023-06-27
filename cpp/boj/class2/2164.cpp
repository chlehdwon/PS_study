#include <iostream>

using namespace std;
int recursion(int n){
	if(n==1) return 1;
	if(n==2) return 2;
	if(n%2==0) return recursion(n/2)*2;
	else{
		int recurr = recursion((n-1)/2)*2;
		return (recurr+2)%(n-1)!=0 ? (recurr+2)%(n-1) : n-1; 
	}
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n;
	cin>>n;
	cout<<recursion(n)<<"\n";

	return 0;
}