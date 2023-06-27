#include <iostream>
#include <vector>
#include <queue>
#define INF 987654321
#define MAX 100000

using namespace std;
int cost[MAX+1];
int n,k;

void dfs(){
	for(int i=0; i<=MAX; ++i)
		cost[i]=INF;
	cost[n]=0;
	priority_queue<pair<int,int>> pq;

	pq.push(make_pair(0,n));
	
	while(!pq.empty()){
		int now_time = -pq.top().first;
		int now_pos = pq.top().second;
		pq.pop();
		if(now_time>cost[now_pos] || now_time>cost[k]) continue;
		if(now_pos>=k){
			if(cost[k]>now_time+now_pos-k)
				cost[k]=now_time+now_pos-k;
			continue;
		}
		int temp = now_pos;
		while(temp>0 && temp<k){
			if(temp*2 <= MAX && cost[temp*2]>now_time){
				cost[temp*2]=now_time;
				pq.push(make_pair(-now_time, temp*2));
				
			}
			temp*=2;
		}
		if(now_pos<MAX && cost[now_pos+1]>now_time+1){
			cost[now_pos+1]=now_time+1;
			pq.push(make_pair(-(now_time+1), now_pos+1));
		}
		if(now_pos>0 && cost[now_pos-1]>now_time+1){
			cost[now_pos-1]=now_time+1;
			pq.push(make_pair(-(now_time+1), now_pos-1));
		}
	}
	return;
	
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n >> k;
	dfs();
	cout << cost[k] << '\n';
	
	return 0;
}

/*
#include <iostream>
#include <deque>
#include <stdio.h>
#include <cstring> // memset
 
using namespace std;
 
#define MAX_SIZE 100000+1
 
int N, K;
int visited[MAX_SIZE];
 
int bfs() {
    deque<int> dq;
    dq.push_back(N);
    visited[N] = 1;
    while (!dq.empty()) {
         // 덱의 앞의 요소들부터 꺼내옴
        int pos_x = dq.front();
        dq.pop_front();
 
        if(pos_x == K) return visited[K] - 1;
 
        // 순간이동은 덱의 앞쪽에 집어넣음.
        if (pos_x * 2 < MAX_SIZE && !visited[pos_x * 2]) {
            dq.push_front(pos_x * 2);
            visited[pos_x * 2] = visited[pos_x];
        }
 
        // 걷는이동은 덱의 뒤쪽에 집어넣음.
        if (pos_x + 1 < MAX_SIZE && !visited[pos_x + 1]) {
            dq.push_back(pos_x + 1);
            visited[pos_x + 1] = visited[pos_x] + 1;
        }
 
        // 걷는이동은 덱의 뒤쪽에 집어넣음.
        if (pos_x - 1 >= 0 && !visited[pos_x - 1]) {
            dq.push_back(pos_x - 1);
            visited[pos_x - 1] = visited[pos_x] + 1;
        }
    }
}
 
int main() {
    scanf("%d %d", &N, &K);
    printf("%d\n", bfs());
    return 0;
}
*/