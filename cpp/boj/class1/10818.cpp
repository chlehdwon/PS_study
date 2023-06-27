#include <cstdio>

int main(){
	int n, num, max=-1000001, min=1000001;
	scanf("%d", &n);
	while(n--){
		scanf("%d", &num);
		if(num<min) min=num;
		if(num>max) max=num;
	}
	
	printf("%d %d\n", min, max);
	
	return 0;
}