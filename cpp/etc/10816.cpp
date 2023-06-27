#include <iostream>
#include <unordered_map>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m,num;
	unordered_map<int, int> counter;
	cin>>n;
	for(int i=0; i<n; ++i){
		cin>>num;
		if(counter.find(num)==counter.end()){
			counter[num]=1;
		}
		else{
			counter[num]+=1;
		}
	}
	cin>>m;
	cin>>num;
	cout<<counter[num];
	for(int j=1; j<m; ++j){
		cin>>num;
		cout<<" "<<counter[num];
	}
	cout<<"\n";
	
	
	return 0;
}