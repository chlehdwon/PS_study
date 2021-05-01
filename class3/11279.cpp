#include <iostream>
#include <set>
#include <queue>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,inst;
	priority_queue<int> pq;
	cin >> n;
	while(n--){
		cin >> inst;
		if(inst==0){
			if(pq.empty()) cout << 0 << '\n';
			else{
				cout << pq.top() << '\n';
				pq.pop();
			}
		}
		else{
			pq.push(inst);
		}
	}

	return 0;
}


/*
using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,inst;
	multiset<int> heap;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> inst;
		if(inst==0){
			if(heap.empty()) cout << 0 << '\n';
			else{
				auto itr = heap.begin();
				cout << -1*(*itr) << '\n';
				heap.erase(itr);
			}
		}
		else{
			heap.insert(-inst);
		}
	}
	
	return 0;
}
*/