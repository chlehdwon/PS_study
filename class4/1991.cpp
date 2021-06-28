#include <iostream>
#include <vector>

using namespace std;
vector<char> map[26];
int n;

string preorder(char c){
	char left_ele = map[c-'A'][0];
	char right_ele = map[c-'A'][1];
	string left = left_ele!='.' ? preorder(left_ele) : "";
	string right = right_ele!='.' ? preorder(right_ele) : "";
	
	return c+left+right;
}

string inorder(char c){
	char left_ele = map[c-'A'][0];
	char right_ele = map[c-'A'][1];
	string left = left_ele!='.' ? inorder(left_ele) : "";
	string right = right_ele!='.' ? inorder(right_ele) : "";
	
	return left+c+right;
}

string postorder(char c){
	char left_ele = map[c-'A'][0];
	char right_ele = map[c-'A'][1];
	string left = left_ele!='.' ? postorder(left_ele) : "";
	string right = right_ele!='.' ? postorder(right_ele) : "";
	
	return left+right+c;
}

int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	cin >> n;
	for(int i=0; i<n; ++i){
		char x,y,z;
		cin >> x >> y >> z;
		map[x-'A'].push_back(y);
		map[x-'A'].push_back(z);
	}
	cout << preorder('A') << "\n" << inorder('A') << "\n" << postorder('A') << "\n";
	
	
	return 0;
}