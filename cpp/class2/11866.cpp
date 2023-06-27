#include <iostream>

using namespace std;

int main() 
{
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int N, K;
	queue<int> q;
	cin >> N >> K;
 
	for (int i = 1; N >= i; i++) {
		q.push(i);
	}
	
	cout << "<";
	while (!q.empty()) {
		for (int i = 0; i < K - 1; i++) {
			q.push(q.front());
			q.pop();
		}
 
		cout << q.front();
		q.pop();
 
		if (!q.empty()) {
			cout << ", ";
		}
 
	}
	cout << ">" << endl;
 
	return 0;
}

/*
int main(){
	int n,k,temp;
	cin >> n >> k;
	cout << "<";
	for(int i=0; i<n; ++i){
		if(n-i<k) temp = k%(n-i)>0 ? k%(n-i) : n-i;
		else temp=k;
		for(int j=i-1; j>=0; --j){
			temp+=k;
			temp = temp%(n-j)>0 ? temp%(n-j) : n-j;
		}
		if(i==n-1) cout << temp << ">\n";
		else cout << temp << ", ";
	}
	
	return 0;
}
*/