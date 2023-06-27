#include <iostream>
#include <cstring>

#include <iostream>
#include <string>
using namespace std;
int n, m; //숫자 배열

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
	int m, i, num, arr=0;
	cin >> m;
	string com;
	for (i = 0; i < m; i++) {
		cin >> com;
		switch(com[0]) {
			case 'a':
				if (com[1] == 'd') { //add
					cin >> num;
					arr |= (1 << (num - 1));
				}
				else { //all
					arr = (1 << 20) - 1;
				}
				break;
			
			case 'c': //check;
				cin >> num;
				if ((arr & (1 << (num - 1)))) {
					cout << "1\n";
				}
				else cout << "0\n";
				break;

			case 'e': //empty
				arr = 0;
				break;

			case 'r': //remove
				cin >> num;
				arr &= ~(1 << (num - 1));
				break;

			case 't':
				cin >> num;
				arr ^= (1 << (num - 1));
				break;
		}
	}
}

/*
using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n, x;
	cin >> n;
	bool *set = new bool[21]{0};
	for(int i=0; i<n; ++i){
		string inst;
		cin >> inst;
		if(inst=="add"){
			cin >> x; x-=1;
			if(set[x]==0) set[x]=1;
		}
		else if(inst=="remove"){
			cin >> x; x-=1;
			if(set[x]==1) set[x]=0;
		}
		else if(inst=="check"){
			cin >> x; x-=1;
			cout << set[x] << "\n";
		}
		else if(inst=="toggle"){
			cin >> x; x-=1;
			if(set[x]==0) set[x]=1;
			else set[x]=0;
		}
		else if(inst=="all"){
			memset(set, true, sizeof(set));
		}
		else if(inst=="empty"){
			memset(set, false, sizeof(set));
		}
		else{
			cout<<"wrong input\n";
			break;
		}
	}

	delete[] set;
	return 0;
}
*/