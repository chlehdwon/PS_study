#include <iostream>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	
	int n, max=2;
	cin >> n;
	int *testcase = new int[n];
	for(int i=0; i<n; ++i){
		int num;
		cin >> num;
		if(num>max) max=num;
		testcase[i]=num;
	}
	int pibo[40][2];
	pibo[0][0]=1; pibo[0][1]=0;
	pibo[1][0]=0; pibo[1][1]=1;
	for(int i=2; i<=max; ++i){
		pibo[i][0]=pibo[i-1][0]+pibo[i-2][0];
		pibo[i][1]=pibo[i-1][1]+pibo[i-2][1];
	}
	for(int i=0; i<n; ++i){
		int num = testcase[i];
		cout << pibo[num][0] << " " << pibo[num][1] << "\n";
	}
	
	delete[] testcase;
	return 0;
}