#include <iostream>
#include <vector>
#include <map>
#include <algorithm>


using namespace std;
typedef pair<int, string> type;


int main(){	
	ios::sync_with_stdio(false);
    cin.tie(0);
	
	int n, age;
	string name;
	cin >> n;
	multimap<int, string> v;
	for(int i=0; i<n; ++i){
		cin >> age >> name;
		v.insert(type(age, name));
	}
	
	for(auto& i:v){
		cout << i.first << " " << i.second << "\n";
	}
	
	return 0;
}
