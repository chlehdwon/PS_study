#include <iostream>
#include <set>

using namespace std;

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> m;
		multiset<int> dq;
		for(int j=0; j<m; ++j){
			char inst;
			int num;
			cin >> inst >> num;
			if(inst=='I'){
				dq.insert(num);
			}
			if(inst=='D'){
				if(!dq.empty()){
					if(num==-1){
						auto begin = dq.begin();
						dq.erase(begin);
					}
					else{
						auto end = dq.end();
						--end;
						dq.erase(end);
					}
				}
				
			}
		}
		if(dq.empty()) cout << "EMPTY" << '\n';
		else{
			auto itr = dq.end();
			--itr;
			cout << *itr << " " << *dq.begin() << '\n';
		}
	}
	
	return 0;
}

/*
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int k;
    cin >> k;
    map<int, int> mp;
    while (k--) {
      char ch;
      cin >> ch;
      if (ch == 'I') {
        int n;
        cin >> n;
        ++mp[n];
      } else {
        int x;
        cin >> x;
        if (mp.empty()) {
          continue;
        }
        if (x == -1) {
          auto it = mp.begin();
          if (--(it->second) == 0) {
            mp.erase(it);
          }
        } else {
          auto it = prev(mp.end());
          if (--(it->second) == 0) {
            mp.erase(it);
          }
        }
      }
    }
    if (mp.empty()) {
      cout << "EMPTY" << '\n';
    } else {
      cout << prev(mp.end())->first << " " << mp.begin()->first << '\n';
    }
  }
  return 0;
}
*/