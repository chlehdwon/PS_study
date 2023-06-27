#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef pair<int, int> ints;

int main(){	
	ios::sync_with_stdio(false);
    cin.tie(0);
	int n, x, y;
	cin>>n;
	vector<ints> vec;
	for(int i=0; i<n; ++i){
		cin >> x >> y;
		vec.push_back(ints(x,y));
	}
	sort(vec.begin(), vec.end());
	for(auto i:vec){
		cout << i.first << " " << i.second << "\n";
	}
	
	return 0;
}

/*
int main()
{
	cin.tie(0); ios_base::sync_with_stdio(0);
	pair<int, int> v[100000];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> v[i].first >> v[i].second;
	}
	sort(v, v+n);
	for(int i = 0; i < n; i++)
		cout << v[i].first << " " << v[i].second << '\n';
	return 0;
}
*/