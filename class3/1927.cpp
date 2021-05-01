#include <iostream>
#include <functional>
#include <queue>

using namespace std;
priority_queue<int, vector<int>, greater<int>> pq;
int n;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	for(int i=0; i<n; ++i){
		int num;
		cin >> num;
		if(num==0){
			if(pq.empty()) cout << 0 << '\n';
			else{
				cout << pq.top() << '\n';
				pq.pop();
			}
		}
		else{
			pq.push(num);
		}
	}
	return 0;
}