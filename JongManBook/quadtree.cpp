#include <iostream>
#include <vector>
#include <string>

using namespace std;
string reverse(string tree){
	if(tree[0]!='x')
		return tree;

	int count=1;
	int target=4;
	int index[4];
	for(int i=0; i<tree.size(); ++i){
		if(count==target){
			index[4-target]=i;
			target--;
		}
		count--;
		if(tree[i]=='x')
			count+=4;
	}
	string quad1 = tree.substr(index[0],index[1]-index[0]);
	string quad2 = tree.substr(index[1],index[2]-index[1]);
	string quad3 = tree.substr(index[2],index[3]-index[2]);
	string quad4 = tree.substr(index[3],tree.size()-index[3]);
	
	return 'x'+reverse(quad3)+reverse(quad4)+reverse(quad1)+reverse(quad2);
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int n;
	string tree;
	string reversed_tree;
	cin >> n;
	for(int i=0; i<n; ++i){
		cin >> tree;
		reversed_tree = reverse(tree);
		cout << reversed_tree << '\n';
	}
	
	return 0;
}