#include <cstdio>

int main(){
	int x,y,w,h,min=0;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	
	int min_x = w-x>=x ? x : w-x;
	int min_y = h-y>=y ? y : h-y;
	min = min_x <= min_y ? min_x : min_y;
	
	printf("%d\n", min);
	
	return 0;
}