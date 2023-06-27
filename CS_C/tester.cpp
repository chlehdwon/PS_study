#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	auto cmp = [](pair<int,int> left, pair<int,int> right) {return left.second > right.second;};
	priority_queue<pair<int,int>,vector<pair<int,int>>,decltype(cmp)> pq1(cmp);
	priority_queue<pair<int,int>> pq2;
	pq1.push(make_pair(1,3));
	pq2.push(make_pair(-3,1));
	pq1.push(make_pair(2,4));
	pq2.push(make_pair(-4,2));
	pq1.push(make_pair(3,2));
	pq2.push(make_pair(-2,3));
	while(!pq1.empty()){
		cout << pq1.top().first << " " << pq1.top().second << '\n';
		pq1.pop();
	}
	while(!pq2.empty()){
		cout << pq2.top().first << " " << pq2.top().second << '\n';
		pq2.pop();
	}
		
		
	return 0;
}