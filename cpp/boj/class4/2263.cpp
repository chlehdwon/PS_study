#include <iostream>
#include <vector>

using namespace std;
int Index[100001];
int inorder[100001];
int postorder[100001];

int n;

void pre(int is, int ps, int len){
	if(len==0) return;
	int parent = postorder[ps+len-1];
	int idx = Index[postorder[ps+len-1]]-is;
	cout << parent << ' ';
	pre(is,ps,idx);
	pre(is+idx+1,ps+idx,len-idx-1);
	return;
}


int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	for(int i=1; i<=n; ++i){
		cin >> inorder[i];
		Index[inorder[i]] = i;
	}
	for(int i=1; i<=n; ++i){
		cin >> postorder[i]; 
	}
	
	pre(1,1,n);
	cout << '\n';
	
	return 0;
}
