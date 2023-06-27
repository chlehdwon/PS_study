#include <iostream>
#include <vector>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n, x, size=0;
	vector<int> my_stack;
	string inst;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> inst;
		if(inst=="push"){
			cin >> x;
			my_stack.push_back(x); ++size;
		}
		else if(inst=="top"){
			if(size)
					cout << my_stack[size-1] << '\n';
			else
				cout << "-1\n";
		}
		else if(inst=="size"){
			cout << size << '\n';
		}
		else if(inst=="empty"){
			if(size)
					cout << "0\n";
			else
				cout << "1\n";
		}
		else{
			if(size){
				cout << my_stack[size-1] << '\n';
				--size; my_stack.erase(my_stack.end()-1);
			}
			else
				cout << "-1\n";
		}
	}
	
	return 0;
}