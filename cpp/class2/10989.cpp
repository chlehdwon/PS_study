#include <cstdio>
#define MAX 100000

int main(){
	int counts[MAX]={0};
	int n=0, num=0, j;

	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &num);
		counts[num-1]+=1;
	}
	
	for(int i=0; i<MAX; i++){
		for(int j=0; j<counts[i]; j++){
			printf("%d\n", j+1);
		}
	}

	return 0;
}