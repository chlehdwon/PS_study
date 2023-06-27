#include <cstdio>

int main(){
	int max = 0, n;
	long double sum = 0;
	int scores[1000];
	scanf("%d", &n);
	for(int i=0; i<n; ++i){
		scanf("%d", &scores[i]);
		sum += scores[i];
		if(max<scores[i]) max=scores[i];
	}
	
	printf("%Lf\n", ((sum*100)/(max*n)));
}