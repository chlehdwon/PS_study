#include <iostream>
#include <queue>
#include <unordered_map>
#include <functional>
#include <algorithm>

using namespace std;

int main(void) {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cout.tie(NULL);

	int n;
	cin >> n;
	vector<pair<int,int>> arr(n);
	vector<int> result(n);
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].first;
		arr[i].second = i;
	}
	sort(arr.begin(), arr.end(),less<pair<int,int>>());
	//개수 미리 세두기
	int pre = arr[0].first;
	int Count = 0;
	for (int i = 0; i < n; i++)
	{
		if (pre != arr[i].first) {
			Count++;
			pre = arr[i].first;
		}
		result[arr[i].second] = Count;
	}
	//입력순서대로 값저장되어 있음
	for (int i = 0; i < n; i++)
	{
		cout << result[i] << " ";
	}
}


/*
using namespace std;
int n, num, now_val, prev_val, ranking=0;
priority_queue<int, vector<int>, greater<int>> pq;
unordered_map<int, int> coord;
int arr[1000000];

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> num;
		arr[i]=num;
		pq.push(num);
	}
	prev_val = pq.top();
	while(!pq.empty()){
		now_val = pq.top();
		if(prev_val!=now_val){
			ranking+=1;
			coord[now_val]=ranking;
		}
		prev_val = now_val;
		pq.pop();
	}
	for(int i=0; i<n; ++i){
		cout << coord[arr[i]] << " ";
	}
	cout << '\n';
	

	return 0;
}
*/