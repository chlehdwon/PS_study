#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int fence[20000];

int max_area(int left, int right){
	if(right==left){
		return fence[left];
	}
	int mid = (left+right)/2;
	int left_max = max_area(left,mid);
	int right_max = max_area(mid+1,right);
	int area = max(left_max, right_max);
	int lo = mid, hi = mid+1;
	int height = min(fence[lo],fence[hi]);
	area = max(area, 2*height);
	while(lo>left || hi<right){
		if(hi<right && (lo==left || fence[lo-1]<fence[hi+1])){
			++hi;
			height = min(height, fence[hi]);
		}
		else{
			--lo;
			height = min(height, fence[lo]);
		}
		
		area = max(area, height*(hi-lo+1));
	}
	
	return area;
}


int main(){
	ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
	int c,n;
	cin >> c;
	for(int i=0; i<c; ++i){
		cin >> n;
		memset(fence,0,sizeof(fence));
		for(int j=0; j<n; ++j){
			cin >> fence[j];
		}
		cout << max_area(0,n-1) << '\n';
	}
	
	
	return 0;
}