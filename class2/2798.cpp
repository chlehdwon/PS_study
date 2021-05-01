#include <iostream>

using namespace std;
int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n,m;
	cin>>n>>m;
	int min=m;
	int* arr = new int[n];
	for(int i=0; i<n; ++i){
		cin>>arr[i];
	}
	for(int i=0; i<n-2; ++i){
		for(int j=i+1; j<n-1; ++j){
			for(int k=j+1; k<n; ++k){
				int sum=arr[i]+arr[j]+arr[k];
				if(sum==m){
					cout<<m<<"\n";
					return 0;
				}
				else if(sum<m) min = min>m-sum ? m-sum : min;
			}
		}
	}
	cout<<m-min<<"\n";
	delete[] arr;
	
	return 0;
}