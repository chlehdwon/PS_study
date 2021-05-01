#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>
#include <string>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	unordered_map<string, int> nametonum;
	
	cin >> n >> m;
	string* names = new string[n+1];
	for(int i=1; i<=n; ++i){
		cin >> names[i];
		nametonum.insert(pair<string, int>(names[i], i));
	}
	for(int i=0; i<m; ++i){
		string search;
		cin >> search;
		if(search[0]>='A' && search[0]<='Z'){
			cout << nametonum[search] << "\n";
		}
		else{
			cout << names[stoi(search)] << "\n";
		}
	}
	
	return 0;
}

/*
using namespace std;
unordered_map<string, int> um1;
unordered_map<int, string> um2;
int N, M;
int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	string s;
	for (int i = 1; i <= N; i++)
		cin >> s, um1[s] = i, um2[i] = s;
	while (cin >> s)
		if (isdigit(s[0]))
			cout << um2[stoi(s)] << '\n';
		else
			cout << um1[s] << '\n';
	return 0;
}
*/