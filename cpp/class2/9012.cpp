#include <iostream>
#include <stack>

using namespace std;
void ps_check(string& ps){
	stack<char> stack;
	for(char& p:ps){
		if(p=='(') stack.push(p);
		else{
			if(stack.empty()){
				cout<<"NO\n";
				return;
			}
			else stack.pop();
		}
	}


	if(stack.empty()) cout<<"YES\n";
	else cout<<"NO\n";

	return;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n;
	cin>>n;
	stack<string> stack;
	for(int i=0; i<n; ++i){
		string ps;
		cin>>ps;
		ps_check(ps);
	}
	
	return 0;
}
