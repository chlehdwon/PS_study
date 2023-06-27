#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0);
	
	int n, num;
	cin >> n;
	vector<int> vec;
	for(int i=0; i<n; i++){
		cin >> num;
		vec.push_back(num);
	}
	sort(vec.begin(), vec.end());
	for(int i=0; i<n; i++){
		cout << vec[i] << "\n";
	}
	
	return 0;
}


