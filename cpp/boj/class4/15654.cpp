#include <iostream>
#include <vector>
#include <algorithm> 

using namespace std;

void sol(vector<bool>& visited, vector<int> nums, vector<int> perm, int depth){
	if(depth==perm.size()){
		for(int i=0; i<perm.size(); ++i){
			cout << perm[i] << " ";
		}
		cout << '\n';
		return;
	}
	for(int i=0; i<nums.size(); ++i){
		if(visited[i]==true)
			continue;
		visited[i] = true;
		perm[depth] = nums[i];
		sol(visited,nums,perm,depth+1);
		visited[i] = false;
	}
	
}


int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	
	int n,m;
	cin >> n >> m;
	vector<int> nums{};
	for(int i=0; i<n; ++i){
		int num;
		cin >> num;
		nums.push_back(num);
	}
	sort(nums.begin(), nums.end());
	vector<bool> visited(n);
	vector<int> perm(m);
	sol(visited, nums, perm, 0);
	
	return 0;
}