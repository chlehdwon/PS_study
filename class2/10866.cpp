#include <iostream>
#include <deque>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n, x, size=0;
	deque<int> my_queue;
	string inst;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> inst;
		if(inst=="push_front"){
			cin >> x;
			my_queue.push_front(x); ++size;
		}
		else if(inst=="push_back"){
			cin >> x;
			my_queue.push_back(x); ++size;
		}
		else if(inst=="pop_front"){
			if(size){
				cout << my_queue[0] << '\n';
				--size; my_queue.pop_front();
			}
			else
				cout << "-1\n";
		}
		else if(inst=="pop_back"){
			if(size){
				cout << my_queue[size-1] << '\n';
				--size; my_queue.pop_back();
			}
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
		else if(inst=="front"){
			if(size)
					cout << my_queue[0] << '\n';
			else
				cout << "-1\n";
		}
		else if(inst=="back"){
			if(size)
					cout << my_queue[size-1] << '\n';
			else
				cout << "-1\n";
		}
	}
	
	return 0;
}